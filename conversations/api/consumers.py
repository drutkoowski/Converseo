from channels.db import database_sync_to_async
from django.db.models import Q
from django.db.models.functions import Now
from accounts.api.serializers import AccountSerializer
from accounts.models import Account
from conversations.api.serializers import QueueSerializer, ConversationSerializer, MessageSerializer
from conversations.models import Conversation, SearchQueue, Message, Match
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework import permissions
import json


class QueueConsumer(GenericAsyncAPIConsumer):
    serializer_class = QueueSerializer
    permission_classes = (permissions.AllowAny,)

    @database_sync_to_async
    def get_user_by_id(self, pk):
        return Account.objects.get(pk=pk)

    @database_sync_to_async
    def create_search_queue(self, user):
        sq = SearchQueue.objects.create(user=user)
        sq.save()
        return sq

    @database_sync_to_async
    def create_match(self, user, talker):
        match = Match.objects.create()
        match.users.add(talker)
        match.users.add(user)
        match.save()
        return match

    @database_sync_to_async
    def get_match(self, match_id):
        try:
            return Match.objects.get(pk=match_id)
        except:
            return None

    @database_sync_to_async
    def save_user_choice(self, match, choice, user):
        if choice:
            match.accepted_by.add(user)
        else:
            match.declined_by.add(user)
        match.save()

    @database_sync_to_async
    def check_acceptance(self, match):
        if match:
            if match.accepted_by.all().count() == 2:
                match.delete()
                return True
            if match.declined_by.all().count() > 0:
                match.delete()
                return False
            else:
                return None


    @database_sync_to_async
    def get_random_talker(self, user):
        sq = SearchQueue.objects.exclude(Q(user=user) | Q(expires_at__lte=Now())).last()
        if sq is not None:
            user_randomized = Account.objects.get(username=sq.user.username)
            search_queues = SearchQueue.objects.filter(Q(user=user) | Q(user=user_randomized)).all()
            for sq in search_queues:
                sq.delete()
            return user_randomized
        else:
            return None

    @database_sync_to_async
    def delete_search_query(self, user):
        search_queues = SearchQueue.objects.filter(user=user).all()
        for sq in search_queues:
            sq.delete()

    @database_sync_to_async
    def create_conversation_room(self, user, talker):
        conversation = Conversation()
        conversation.save()
        conversation.users.add(talker)
        conversation.users.add(user)
        conversation.save()
        return conversation

    @database_sync_to_async
    def check_talked_already(self, user, talker):
        conversation = Conversation.objects.filter(users=user).filter(users=talker).first()
        if conversation:
            return conversation
        else:
            return None

    # jesli jakis nowy user sie polaczy z systemem, subskrybuje model change
    async def connect(self, **kwargs):
        # await self.channel_layer.group_add() // lub group_discard dla disconnect
        user = self.scope['user']
        if user is not None:
            await self.accept()
            self.room_group_name = user.username

            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            #
            await self.create_search_queue(user)
            random_talker = await self.get_random_talker(user)
            if random_talker is not None:
                # is_talked_already = await self.check_talked_already(user, random_talker)
                # if is_talked_already is None:
                #     conversation = await self.create_conversation_room(user, random_talker)
                # else:
                #     conversation = is_talked_already
                match = await self.create_match(user, random_talker)
                await self.channel_layer.group_send(
                    "{}".format(random_talker.username),
                    {
                        'type': 'send_message',
                        'random_talker': AccountSerializer(instance=user).data,
                        'matchId': match.pk,
                        'talkerId': user.pk,
                        'subject': 'found'
                    }
                )
                await self.channel_layer.group_send(
                    "{}".format(user.username),
                    {
                        'type': 'send_message',
                        'random_talker': AccountSerializer(instance=random_talker).data,
                        'matchId': match.pk,
                        'talkerId': random_talker.pk,
                        'subject': 'found'
                    }
                )

    async def disconnect(self, code):
        await self.delete_search_query(self.scope['user'])
        self.channel_layer.group_discard(self.room_group_name,
                                         self.channel_name)
        await self.close()

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        data = json.loads(text_data)
        choice = data['choice']
        match_id = data['matchId']
        talker_id = data['talkerId']
        user = self.scope['user']
        match = await self.get_match(match_id)
        talker = await self.get_user_by_id(talker_id)
        await self.save_user_choice(match, choice, user)
        is_accepted = await self.check_acceptance(match)
        print('DECYZJA', is_accepted)
        print('talker', talker.username)
        print('JA', user.username)
        if is_accepted:
            is_talked_already = await self.check_talked_already(user, talker)
            if is_talked_already is None:
                conversation = await self.create_conversation_room(user, talker)
            else:
                conversation = is_talked_already
            await self.channel_layer.group_send(
                "{}".format(talker.username),
                {
                    'type': 'send_message',
                    'random_talker': AccountSerializer(instance=user).data,
                    'room_id': conversation.pk,
                    'subject': 'matched'
                }
            )
            await self.channel_layer.group_send(
                "{}".format(user.username),
                {
                    'type': 'send_message',
                    'random_talker': AccountSerializer(instance=talker).data,
                    'room_id': conversation.pk,
                    'subject': 'matched'
                }
            )
        if is_accepted is False:
            await self.channel_layer.group_send(
                "{}".format(talker.username),
                {
                    'type': 'send_message',
                    'random_talker': AccountSerializer(instance=user).data,
                    'subject': 'declined'
                }
            )

    async def send_message(self, event):
        # Receive message from room group
        message = event
        await self.send(text_data=json.dumps({
            'random_talker': message
        }))

    # @model_observer(SearchQueue)  # musze dodac dekorator, funkcja obojetnie jaka nazwa, w parametrze model
    # async def model_change(self, message, observer=None,
    #                        **kwargs):  # jesli jest jakas zmiana w modelu, wysyla json do usera
    #
    #     user = await self.get_user(message['data']['user'])
    #
    #     await self.send_json(message)

    # @model_change.serializer  # dekorator z taka sama nazwa jak funkcja na gorze
    # def model_serialize(self, instance, action, **kwargs):
    #     return dict(data=QueueSerializer(instance=instance).data, action=action.value)


class ConversationConsumer(GenericAsyncAPIConsumer):
    serializer_class = ConversationSerializer
    permission_classes = (permissions.AllowAny,)

    @database_sync_to_async
    def get_user(self, username):
        return Account.objects.get(username=username)

    @database_sync_to_async
    def get_talker_user(self, user, conversation):
        conversation = Conversation.objects.get(pk=conversation.pk)
        users = conversation.users.all()
        for el in users:
            if el != user:
                json_data = json.dumps(AccountSerializer(el).data)
                return json_data

    @database_sync_to_async
    def get_conversation(self, id):
        try:
            return Conversation.objects.get(pk=id)
        except:
            return None

    @database_sync_to_async
    def delete_conversation(self, conversation):
        conversation.delete()

    @database_sync_to_async
    def is_conversation_user(self, conversation, user):
        if user in conversation.users.all():
            return True
        return False

    @database_sync_to_async
    def save_message(self, user, conversation, message):
        message = Message.objects.create(user=user, conversation=conversation, content=message)
        return message

    @database_sync_to_async
    def get_all_messages(self, conversation):
        messages = Message.objects.filter(conversation=conversation).order_by("conversation__created_at").all()
        json_data = json.dumps(MessageSerializer(messages, many=True).data)
        return json_data

    async def connect(self, **kwargs):
        conversation_id = self.scope["url_route"]["kwargs"]['id']
        conversation = await self.get_conversation(conversation_id)
        if conversation is None:
            await self.accept()
            await self.send_json({'status': 'not found'})
            await self.close()
            return
        user_connecting = self.scope['user']
        is_participant = await self.is_conversation_user(conversation, user_connecting)
        if conversation is not None and is_participant:
            self.room_group_name = f'chat-{conversation_id}'
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            messages = await self.get_all_messages(conversation)
            talker = await self.get_talker_user(user_connecting, conversation)
            await self.accept()
            await self.send_json({'messages': messages, 'status': 'initial', 'talker': talker})
        else:
            await self.accept()
            await self.send_json({'status': 'not found'})
            await self.close()
            return
        #

    async def disconnect(self, code):
        # user = await self.get_user(self.scope["url_route"]["kwargs"]["username"])
        # await self.delete_search_query(self.scope['user'])
        # self.channel_layer.group_discard(self.room_group_name,
        #                                  self.channel_name)
        self.channel_layer.group_discard(self.room_group_name,
                                         self.channel_name)
        await self.close()

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        data = json.loads(text_data)
        close = data['close']
        message = data['message']
        user = self.scope['user']
        conversation = await self.get_conversation(data['conversation_id'])
        if close:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'conversation_notification',
                    'status': 'close'
                }
            )
            await self.delete_conversation(conversation)
            self.channel_layer.group_discard(self.room_group_name,
                                             self.channel_name)
            await self.close()

        else:
            message = await self.save_message(user, conversation, message)

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': MessageSerializer(instance=message).data,
                    'status': 'update'
                }
            )

    async def conversation_notification(self, event):
        status = event['status']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'status': status
        }))

    async def chat_message(self, event):
        message = event['message']
        status = event['status']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'status': status
        }))

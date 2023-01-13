import json

from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from django.db.models import Q
from django.db.models.functions import Now
from accounts.api.serializers import AccountSerializer
from accounts.models import Account
from conversations.api.serializers import QueueSerializer, ConversationSerializer, MessageSerializer
from conversations.models import Conversation, SearchQueue, Message
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework import permissions
import json

class QueueConsumer(GenericAsyncAPIConsumer):
    serializer_class = QueueSerializer
    permission_classes = (permissions.AllowAny,)

    # @database_sync_to_async
    # def get_user(self, username):
    #     return Account.objects.get(username=username)

    @database_sync_to_async
    def create_search_queue(self, user):
        return SearchQueue.objects.create(user=user).save()

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
                conversation = await self.create_conversation_room(user, random_talker)
                await self.channel_layer.group_send(
                    "{}".format(random_talker.username),
                    {
                        'type': 'send_message',
                        'random_talker': AccountSerializer(instance=user).data,
                        'room_id': conversation.pk,
                        'subject': 'found'
                    }
                )
                await self.channel_layer.group_send(
                    "{}".format(user.username),
                    {
                        'type': 'send_message',
                        'random_talker': AccountSerializer(instance=random_talker).data,
                        'room_id': conversation.pk,
                        'subject': 'found'
                    }
                )

    async def disconnect(self, code):
        # user = await self.get_user(self.scope["url_route"]["kwargs"]["username"])
        await self.delete_search_query(self.scope['user'])
        self.channel_layer.group_discard(self.room_group_name,
                                         self.channel_name)
        await self.close()

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
    def get_conversation(self, id):
        return Conversation.objects.get(pk=id)

    @database_sync_to_async
    def is_conversation_user(self, conversation, user):
        if user in conversation.users.all():
            return True
        return False

    @database_sync_to_async
    def save_message(self, user, conversation, message):
        Message.objects.create(user=user, conversation=conversation, content=message)

    @database_sync_to_async
    def get_all_messages(self, conversation):
        messages = Message.objects.filter(conversation=conversation).order_by("conversation__created_at").all()
        json_data = json.dumps({"messages": MessageSerializer(messages, many=True).data})
        return json_data

    async def connect(self, **kwargs):
        conversation_id = self.scope["url_route"]["kwargs"]['id']
        conversation = await self.get_conversation(conversation_id)
        user_connecting = self.scope['user']
        is_participant = await self.is_conversation_user(conversation, user_connecting)
        if conversation is not None and is_participant:
            self.room_group_name = f'chat-{conversation_id}'
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            messages = await self.get_all_messages(conversation)
            await self.accept()
            await self.send_json(messages)

        #

    async def disconnect(self, code):
        # user = await self.get_user(self.scope["url_route"]["kwargs"]["username"])
        # await self.delete_search_query(self.scope['user'])
        # self.channel_layer.group_discard(self.room_group_name,
        #                                  self.channel_name)
        await self.close()

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        data = json.loads(text_data)
        print(data)
        message = data['message']
        user = self.scope['user']
        conversation = await self.get_conversation(data['conversation_id'])
        await self.save_message(user, conversation, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': AccountSerializer(instance=user).data
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user = event['user']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user
        }))
import json

from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from django.db.models import Q
from django.db.models.functions import Now

from accounts.api.serializers import AccountSerializer
from accounts.models import Account
from conversations.api.serializers import QueueSerializer
from conversations.models import Conversation, SearchQueue

from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework import permissions


class QueueConsumer(GenericAsyncAPIConsumer):
    serializer_class = QueueSerializer
    permission_classes = (permissions.AllowAny,)

    @database_sync_to_async
    def get_user(self, username):
        return Account.objects.get(username=username)

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

    # jesli jakis nowy user sie polaczy z systemem, subskrybuje model change
    async def connect(self, **kwargs):
        # await self.channel_layer.group_add() // lub group_discard dla disconnect
        username = self.scope["url_route"]["kwargs"]["username"]
        await self.accept()
        self.room_group_name = username

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        #
        user = await self.get_user(username)
        await self.create_search_queue(user)
        random_talker = await self.get_random_talker(user)
        if random_talker is not None:
            await self.channel_layer.group_send(
                "{}".format(random_talker.username),
                {
                    'type': 'send_message',
                    'random_talker': AccountSerializer(instance=user).data,
                    'room_id': 231,
                    'subject': 'found'
                }
            )
            await self.channel_layer.group_send(
                "{}".format(username),
                {
                    'type': 'send_message',
                    'random_talker': AccountSerializer(instance=random_talker).data,
                    'room_id': 231,
                    'subject': 'found'
                }
            )
            # await self.send_json({'random_talker': AccountSerializer(instance=random_talker).data, 'room_id': 231})
        # await super().connect()

    async def disconnect(self, code):
        user = await self.get_user(self.scope["url_route"]["kwargs"]["username"])
        await self.delete_search_query(user)
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

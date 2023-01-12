from conversations.models import Conversation

from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework import permissions


# class PostConsumer(ListModelMixin, GenericAsyncAPIConsumer):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = (permissions.AllowAny,)
#
#     # jesli jakis nowy user sie polaczy z systemem, subskrybuje model change
#     async def connect(self, **kwargs):
#         # await self.channel_layer.group_add() // lub group_discard dla disconnect
#         await self.model_change.subscribe()
#         await super().connect()
#
#     @model_observer(Post)  # musze dodac dekorator, funkcja obojetnie jaka nazwa, w parametrze model
#     async def model_change(self, message, observer=None,
#                            **kwargs):  # jesli jest jakas zmiana w modelu, wysyla json do usera
#         await self.send_json(message)
#
#     @model_change.serializer  # dekorator z taka sama nazwa jak funkcja na gorze
#     def model_serialize(self, instance, action, **kwargs):
#         return dict(data=PostSerializer(instance=instance).data, action=action.value)


# class QueueConsumer(GenericAsyncAPIConsumer):
#     serializer_class = PostSerializer
#     permission_classes = (permissions.AllowAny,)
#
#     # jesli jakis nowy user sie polaczy z systemem, subskrybuje model change
#     async def connect(self, **kwargs):
#         # await self.channel_layer.group_add() // lub group_discard dla disconnect
#         await self.model_change.subscribe()
#         await super().connect()
#
#     @model_observer(Post)  # musze dodac dekorator, funkcja obojetnie jaka nazwa, w parametrze model
#     async def model_change(self, message, observer=None,
#                            **kwargs):  # jesli jest jakas zmiana w modelu, wysyla json do usera
#         await self.send_json(message)
#
#     @model_change.serializer  # dekorator z taka sama nazwa jak funkcja na gorze
#     def model_serialize(self, instance, action, **kwargs):
#         return dict(data=PostSerializer(instance=instance).data, action=action.value)


# class ConversationConsumer(GenericAsyncAPIConsumer):
#     queryset = Conversation.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = (permissions.AllowAny,)
#
#     # jesli jakis nowy user sie polaczy z systemem, subskrybuje model change
#     async def connect(self, **kwargs):
#         # await self.channel_layer.group_add() // lub group_discard dla disconnect
#         await self.model_change.subscribe()
#         await super().connect()
#
#     @model_observer(Post)  # musze dodac dekorator, funkcja obojetnie jaka nazwa, w parametrze model
#     async def model_change(self, message, observer=None,
#                            **kwargs):  # jesli jest jakas zmiana w modelu, wysyla json do usera
#         await self.send_json(message)
#
#     @model_change.serializer  # dekorator z taka sama nazwa jak funkcja na gorze
#     def model_serialize(self, instance, action, **kwargs):
#         return dict(data=PostSerializer(instance=instance).data, action=action.value)

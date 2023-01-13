from django.urls import re_path

from conversations.api import consumers

websocket_urlpatterns = [
    re_path(r"^ws/queue/(?P<username>\w+)/$", consumers.QueueConsumer.as_asgi()),
    re_path(r"^ws/conversations/(?P<id>\w+)/$", consumers.ConversationConsumer.as_asgi()),
    # re_path(r"^ws/conversations/$", consumers.ConversationConsumer.as_asgi())
]
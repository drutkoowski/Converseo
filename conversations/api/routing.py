from django.urls import re_path

from conversations.api import consumers

websocket_urlpatterns = [
    # re_path(r"^ws/queue/$", consumers.QueueConsumer.as_asgi()),
    # re_path(r"^ws/conversations/$", consumers.ConversationConsumer.as_asgi())
]
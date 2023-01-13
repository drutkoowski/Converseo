"""
ASGI config for converseo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

#
from channels.routing import ProtocolTypeRouter, URLRouter
from conversations.api.routing import websocket_urlpatterns
from converseo.middleware import JwtAuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': JwtAuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
})

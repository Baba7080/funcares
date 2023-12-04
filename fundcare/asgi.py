"""
ASGI config for fundcare project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import market.routing
from channels.sessions import SessionMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fundcare.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket': SessionMiddlewareStack(
        URLRouter(
            market.routing.websocket_urlpatterns
        )
    )
})
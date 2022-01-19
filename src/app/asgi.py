"""
ASGI config for app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

# mysite/asgi.py
import os

from channels.auth import AuthMiddlewareStack

from django.core.asgi import get_asgi_application
import talkroom.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

django_routing_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            talkroom.routing.websocket_urlpatterns
        )
    ),
})
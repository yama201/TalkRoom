# chat/routing.py
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'ws/talkroom/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]


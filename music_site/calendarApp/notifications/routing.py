from channels.routing import (ProtocolTypeRouter,
                              URLRouter)
from .consumers import NoseyConsumer
from django.urls import path

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("notifications/", NoseyConsumer),
    ])
})
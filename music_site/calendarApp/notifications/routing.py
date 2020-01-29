from channels.routing import (ProtocolTypeRouter,
                              URLRouter)
from .consumers import NotifyConsumer
from django.urls import path

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("notifications/", NotifyConsumer),
    ])
})
from channels.routing import (ProtocolTypeRouter,
                              URLRouter)
from .consumers import NotificationConsumer
from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import (AllowedHostsOriginValidator,
                                         OriginValidator)

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("websocket/", NotificationConsumer)
    ])
})
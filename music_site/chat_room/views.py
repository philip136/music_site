from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.parsers import (MultiPartParser,
                                    FormParser,
                                    JSONParser)
from .models import (Room,
                     Chat)
from .serializer import (RoomSerializer,
                        ChatSerializer,
                        ChatPostSerializer)



class RoomApi(APIView):
    permission_class = [permissions.IsAuthenticated, ]

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response({"data": serializer.data})


class DialogApi(APIView):
    serializer_class = ChatPostSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get(self, request):
        room = request.GET.get("room")
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializer(chat, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        dialog = self.serializer_class(data=request.data)
        if not dialog.is_valid():
            return Response({"status": "Add"})
        dialog.save(user=request.user)
        return Response({"status": "Error"})
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.parsers import (MultiPartParser,
                                    FormParser,
                                    JSONParser)
from .models import (Room,
                     Chat)
from .serializer import (RoomSerializer,
                        ChatSerializer,
                        ChatPostSerializer,
                        UserSerializer)



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
            return Response(status=201)
        dialog.save(user=request.user)
        return Response(status=400)

    
class AddUsersRoom(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        room = request.data.get("room")
        user = request.data.get("user")
        room = Room.objects.get(id=room)
        room.invited.add(user)
        room.save()
        return Response(status=201)
        
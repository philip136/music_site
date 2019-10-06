from rest_framework import serializers
from .models import (Room,
                     Chat)
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
        ]


class RoomSerializer(serializers.ModelSerializer):
    creater = UserSerializer()
    invited = UserSerializer(many=True)

    class Meta:
        model = Room
        fields = [
            'id',
            'creater',
            'invited',
            'date',
        ]


class ChatSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Chat
        fields = [
            'user',
            'text',
            'date',
        ]


class ChatPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = [
            'room',
            'text',
        ]
from rest_framework import serializers
from .models import Room
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
            'creater',
            'invited',
            'date',
        ]
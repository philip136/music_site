from rest_framework import serializers
from music.models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
                  'user',
                  'id',
                  'name_album',
                  'author_album',
                  'genre',
                  'release_date',
                  ]


class AlbumDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
                  'user',
                  'id',
                  'name_album',
                  'author_album',
                  'genre',
                  'release_date',
                  ]

class AlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
                  'name_album',
                  'author_album',
                  'genre',
                  'release_date',
                  ]


class AlbumUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
                  'name_album',
                  'author_album',
                  'genre',
                  ]


from rest_framework import serializers
from music.models import Comments


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
                  'id',
                  'album',
                  'post',
                  'author',
                  'text',
                  'publish_date',
                  ]


class AlbumDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
                    'album',
                    'post',
                    'author',
                    'text',
                  ]

class AlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
                    'album',
                    'post',
                    'author',
                    'text',
                  ]


class AlbumUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
                   'id',
                   'post',
                   'text',
                  ]




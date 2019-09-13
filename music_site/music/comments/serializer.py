from rest_framework import serializers
from music.models import Comments, Album


class CommentSerializer(serializers.ModelSerializer):
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


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
                    'album',
                    'post',
                    'author',
                    'text',
                  ]


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
                   'post',
                   'text',
                  ]
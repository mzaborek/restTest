from rest_framework import serializers
from .models import Movielist, Comment

class MovielistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movielist
        fields = ('id', 'title', 'year', 'runtime', 'released', 'actors', 'season')
        read_only_fields = ('year', 'runtime', 'released', 'actors', 'season')

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('movie', 'commentText')

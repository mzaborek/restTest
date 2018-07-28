from rest_framework import serializers
from .models import Movielist, Comment

class MovielistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movielist
        fields = ('id', 'title', 'year', 'rated', 'released', 'runtime', 'genre', 'director',
                  'writer', 'actors', 'plot', 'language', 'country', 'awards', 'poster', 'ratings',
                  'metascore', 'imdbRating', 'imdbVotes', 'imdbID', 'type', 'dvd', 'boxoffice',
                  'production', 'website', 'season')
        read_only_fields = ('year', 'rated', 'released', 'runtime', 'genre', 'director',
                  'writer', 'actors', 'plot', 'language', 'country', 'awards', 'poster', 'ratings',
                  'metascore', 'imdbRating', 'imdbVotes', 'imdbID', 'type', 'dvd', 'boxoffice',
                  'production', 'website', 'season')

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('movie', 'commentText')

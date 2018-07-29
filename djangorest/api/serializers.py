from rest_framework import serializers

from .models import Movielist, Comment


class MovielistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movielist
        fields = (
            'id', 'Title', 'Year', 'Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Writer', 'Actors', 'Plot',
            'Language', 'Country', 'Awards', 'Poster', 'Ratings', 'Metascore', 'imdbRating', 'imdbVotes',
            'imdbID', 'Type', 'DVD', 'BoxOffice', 'Production', 'Website', 'totalSeasons')
        read_only_fields = ('Year', 'Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Writer', 'Actors', 'Plot',
                            'Language', 'Country', 'Awards', 'Poster', 'Ratings', 'Metascore', 'imdbRating',
                            'imdbVotes',
                            'imdbID', 'Type', 'DVD', 'BoxOffice', 'Production', 'Website', 'totalSeasons')


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('movie', 'commentText')

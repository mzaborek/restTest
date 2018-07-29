from django.shortcuts import render
from rest_framework import generics, status, serializers
from rest_framework.request import override_method

from .serializers import MovielistSerializer, CommentsSerializer
from .models import Movielist, Comment
from rest_framework.response import Response
from .omdb import MovieData
import requests
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.filters import OrderingFilter

# Create your views here.

class CreateMoviesView(generics.ListCreateAPIView):
    queryset = Movielist.objects.all()
    serializer_class = MovielistSerializer
    http_method_names = [u'get', u'post']
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filter_fields = ('year', 'country')
    ordering_fields = ('year', 'metascore')

    # def perform_create(self, serializer):
    #     serializer.save()

    def create(self, request, *args, **kwargs):
        title = request.data['title']
        if not title:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            omdbdata = MovieData().request(title, 10)
        except requests.exceptions.RequestException:
            return Response(status=status.HTTP_408_REQUEST_TIMEOUT)

        #movie not found in omdb database
        if omdbdata['Response'] != "True":
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(
            year=omdbdata['Year'],
            rated=omdbdata['Rated'],
            released=omdbdata['Released'],
            runtime=omdbdata['Runtime'],
            genre=omdbdata['Genre'],
            director=omdbdata['Director'],
            writer=omdbdata['Writer'],
            actors=omdbdata['Actors'],
            plot=omdbdata['Plot'],
            language=omdbdata['Language'],
            country=omdbdata['Country'],
            awards=omdbdata['Awards'],
            poster=omdbdata['Poster'],
            ratings=omdbdata['Ratings'],
            metascore=omdbdata['Metascore'],
            imdbRating=omdbdata['imdbRating'],
            imdbVotes=omdbdata['imdbVotes'],
            imdbID=omdbdata['imdbID'],
            type=omdbdata['Type'],
            dvd=omdbdata['DVD'],
            boxoffice=omdbdata['BoxOffice'],
            production=omdbdata['Production'],
            website=omdbdata['Website'],
            season=omdbdata['Season']
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateCommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    http_method_names = [u'get', u'post']


    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        queryset = Comment.objects.all()
        movie = self.request.query_params.get('movie', None)
        if movie is not None:
            queryset = queryset.filter(movie = movie)

        return queryset
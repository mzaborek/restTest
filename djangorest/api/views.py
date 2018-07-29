import requests
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from .models import Movielist, Comment
from .omdb import MovieData
from .serializers import MovielistSerializer, CommentsSerializer


# Create your views here.

class CreateMoviesView(generics.ListCreateAPIView):
    queryset = Movielist.objects.all()
    serializer_class = MovielistSerializer
    http_method_names = [u'get', u'post']
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filter_fields = ('Year', 'Country')
    ordering_fields = ('Year', 'metascore')

    # def perform_create(self, serializer):
    #     serializer.save()

    def create(self, request, *args, **kwargs):
        title = request.data['Title']
        if not title:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            omdbdata = MovieData().request(title, 10)
        except requests.exceptions.RequestException:
            return Response(status=status.HTTP_408_REQUEST_TIMEOUT)

        # movie not found in omdb database
        if omdbdata['Response'] != "True":
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        omdbdata = {key: value for key, value in omdbdata.items() if key != 'Response'}

        serializer.save(**omdbdata)

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
            queryset = queryset.filter(movie=movie)

        return queryset

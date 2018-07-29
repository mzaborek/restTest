from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Movielist, Comment


# Create your tests here.
class MovieViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movielist_data = {'Title': 'Giant'}

    def test_api_can_create_a_movielist(self):
        """Test if API can create a movie data"""
        response = self.client.post(
            '/movies/',
            self.movielist_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_movielist(self):
        """Test if API can get a movielist data"""
        response = self.client.get('/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ModelTestCase(TestCase):
    def setUp(self):
        self.movielist_title = "Giant"
        self.movielist_title = Movielist(Title=self.movielist_title)

    def test_model_can_create_movielist(self):
        old_count = Movielist.objects.count()
        self.movielist_title.save()
        new_count = Movielist.objects.count()
        self.assertNotEqual(old_count, new_count)


class CommentViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        response = self.client.post(
            '/movies/',
            {'Title': 'Giant'},
            format="json"
        )
        # print("response id = ", response.json()['id'])
        self.movieid = response.json()['id']
        self.comment_data = {'movie': self.movieid, 'commentText': 'bla bla bla BLA!'}

    def test_api_can_create_a_comment(self):
        """Test if API can create a comment data"""
        response = self.client.post(
            '/comments/',
            self.comment_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_comments(self):
        """Test if API can get a comments data"""
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_get_filtered_comments(self):
        response = self.client.get('/comments/', params={'movie': self.movieid})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CommentsModelTestCase(TestCase):
    def setUp(self):
        self.movielist_title = "Giant"
        self.movielist_title = Movielist(Title=self.movielist_title)
        self.movielist_title.save()

        self.commentText = "asdasdasdasda"
        self.comment = Comment(movie=self.movielist_title, commentText=self.commentText)

    def test_model_can_create_comment(self):
        old_count = Comment.objects.count()
        self.comment.save()
        new_count = Comment.objects.count()
        self.assertNotEqual(old_count, new_count)

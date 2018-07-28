from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from django.test import TestCase
from .models import Movielist

# Create your tests here.
class MovieViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movielist_data = {'title' : 'Giant'}
        self.response = self.client.post(
            reverse('create'),
            self.movielist_data,
            format="json"
        )

    def test_api_can_create_a_movielist(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

class ModelTestCase(TestCase):
    def setUp(self):
        self.movielist_title= "Giant"
        self.movielist_title = Movielist(title=self.movielist_title)

    def test_model_can_create_bucketlist(self):
        old_count = Movielist.objects.count()
        self.movielist_title.save()
        new_count = Movielist.objects.count()
        self.assertNotEqual(old_count, new_count)
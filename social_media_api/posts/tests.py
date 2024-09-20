from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Post

CustomUser = get_user_model()

class PostTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_create_post(self):
        url = reverse('post-list')  # The route name of the post list
        data = {'title': 'Test Post', 'content': 'This is a test post'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_posts(self):
        Post.objects.create(author=self.user, title='Test Post', content='This is a test post')
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)  # Check if one post is returned

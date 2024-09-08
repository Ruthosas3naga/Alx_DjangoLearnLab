from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from api.models import Book, Author
from django.contrib.auth.models import User
from api.serializers import BookSerializer, AuthorSerializer


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user and an admin user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.admin_user = User.objects.create_superuser(username='adminuser', password='adminpassword')

        # Create an author
        self.author = Author.objects.create(name='Author 1')
        
        # Create a book instance
        self.book = Book.objects.create(
            title='Test Book',
            author=self.author,
            publication_year=2023
        )

        self.client = APIClient()

    def test_list_books(self):
        """Test retrieving the list of books."""
        url = reverse('list-books')  # Ensure the URL name matches your URL conf
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_authenticated(self):
        """Test creating a new book as an authenticated user."""
        self.client.login(username='testuser', password='testpassword')
        url = reverse('create-book')  # Ensure the URL name matches your URL conf
        data = {
            'title': 'New Book',
            'author': self.author.id,
            'publication_year': 2024
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        """Test that an unauthenticated user cannot create a book."""
        url = reverse('create-book')
        data = {
            'title': 'New Book',
            'author': self.author.id,
            'publication_year': 2024
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book(self):
        """Test updating a book as an authenticated user."""
        self.client.login(username='testuser', password='testpassword')
        url = reverse('update-book', args=[self.book.id])
        data = {
            'title': 'Updated Book',
            'author': self.author.id,
            'publication_year': 2024
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book_as_admin(self):
        """Test deleting a book as an admin user."""
        self.client.login(username='adminuser', password='adminpassword')
        url = reverse('delete-book', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_search_books(self):
        """Test searching for books by title."""
        url = reverse('list-books')
        response = self.client.get(url, {'search': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_filter_books(self):
        """Test filtering books by author."""
        url = reverse('list-books')
        response = self.client.get(url, {'author__name': 'Author 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_order_books(self):
        """Test ordering books by title."""
        url = reverse('list-books')
        response = self.client.get(url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

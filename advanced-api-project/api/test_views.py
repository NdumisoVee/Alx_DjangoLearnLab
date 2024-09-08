from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from api.models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):

        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # book instances for testing
        self.book1 = Book.objects.create(title="Book One", author="Author One", publication_year=2021)
        self.book2 = Book.objects.create(title="Book Two", author="Author Two", publication_year=2020)

    def test_create_book(self):
        """Test creating a new book"""
        url = reverse('book-list')  # Assuming the name of your view is 'book-list'
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'publication_year': 2022,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, 'New Book')

    def test_retrieve_books(self):
        """Test retrieving the list of books"""
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Checking that two books exist

    def test_retrieve_single_book(self):
        """Test retrieving a single book by ID"""
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Book One')

    def test_update_book(self):
        #updating a book
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        data = {
            'title': 'Updated Book',
            'author': 'Updated Author',
            'publication_year': 2022
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')

    def test_delete_book(self):
        #deleting a book
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        #filtering books by author
        url = reverse('book-list')
        response = self.client.get(url, {'author': 'Author One'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author One')

    def test_search_books(self):
        """Test searching books by title"""
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Book One'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_order_books(self):
        """Test ordering books by publication year"""
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'publication_year'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book Two')  # 2020 is before 2021

    def test_authentication_required_for_create(self):
        """Test that authentication is required for creating a book"""
        self.client.logout()
        url = reverse('book-list')
        data = {'title': 'Unauthorized Book', 'author': 'Unauthorized Author', 'publication_year': 2022}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

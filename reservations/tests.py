from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIClient
from .models import MenuItem, TableBooking

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_menu_items(self):
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, 200)

    def test_table_booking(self):
        response = self.client.post('/api/bookings/', {'name': 'John Doe', 'email': 'john@example.com', 'date': '2024-01-01', 'time': '19:00', 'guests': 4})
        self.assertEqual(response.status_code, 201)

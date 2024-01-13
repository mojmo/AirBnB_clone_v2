"""Unit tests for the User class."""
import unittest

from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """Contains unit tests for the User class."""

    def test_user_creation_with_valid_details(self):
        """Test that a User object can be created with valid email,
         password, first name, and last name"""
        user = User(email='test@example.com', password='password',
                    first_name='John', last_name='Doe')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'password')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    def test_user_update_and_save_to_storage(self):
        """Test that a User object can be updated and saved to storage"""
        user = User(email='test@example.com', password='password',
                    first_name='John', last_name='Doe')
        user.save()
        user.first_name = 'Jane'
        user.save()
        self.assertEqual(user.first_name, 'Jane')

    def test_user_creation_with_empty_details(self):
        """Test that a User object can be created with
        empty email, password, first name, and last name"""
        user = User()
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

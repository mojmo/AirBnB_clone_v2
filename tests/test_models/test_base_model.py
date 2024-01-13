"""Unit tests for the BaseModel class."""
import unittest
from datetime import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Contains unit tests for the BaseModel class."""

    def test_base_model_instance_no_arguments(self):
        """
        Test that a BaseModel instance can be created with no arguments
        """
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)

    def test_base_model_instance_keyword_arguments(self):
        """
        Test that a BaseModel instance can be created with keyword arguments
        """
        base_model = BaseModel(created_at='2022-01-01T00:00:00.000')
        self.assertIsInstance(base_model, BaseModel)
        self.assertEqual(base_model.created_at, datetime(2022, 1, 1, 0, 0, 0))

    def test_base_model_instance_invalid_created_at(self):
        """
        Test that a BaseModel instance cannot be created with an
        invalid created_at
        """
        with self.assertRaises(ValueError):
            BaseModel(created_at='invalid_date')

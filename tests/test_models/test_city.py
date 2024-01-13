"""Unit tests for the City class."""
import unittest

from models.city import City


class TestCity(unittest.TestCase):
    """Contains unit tests for the City class."""

    def test_city_instance_with_state_id_and_name_attributes(self):
        """
        Test that a City instance can be created with state_id and
        name attributes
        """
        city = City(state_id="CA", name="San Francisco")
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")

    def test_city_instance_without_state_id_and_name_attributes(self):
        """
        Test that a City instance can be created without state_id and
        name attributes
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_instance_with_non_string_state_id_and_name_attributes(self):
        """
        Test that a City instance can be created with non-string state_id and
        name attributes
        """
        city = City(state_id=123, name=456)
        self.assertEqual(city.state_id, 123)
        self.assertEqual(city.name, 456)

    def test_city_instance_with_empty_state_id_and_name_attributes(self):
        """
        Test that a City instance can be created with empty state_id and
        name attributes
        """
        city = City(state_id="", name="")
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

"""Unit tests for the Place class."""
import unittest

from models.place import Place


class TestPlace(unittest.TestCase):
    """Contains unit tests for the Place class."""

    def test_create_place_with_all_attributes(self):
        """
        test_create_place_with_all_attributes tests that
        when a Place object is
        """
        place = Place(city_id='123', user_id='456', name='Test Place',
                      description='This is a test place',
                      number_rooms=2, number_bathrooms=1, max_guest=4,
                      price_by_night=100.0, latitude=37.7749,
                      longitude=-122.4194, amenity_ids=['wifi', 'pool'])
        self.assertEqual(place.city_id, '123')
        self.assertEqual(place.user_id, '456')
        self.assertEqual(place.name, 'Test Place')
        self.assertEqual(place.description, 'This is a test place')
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100.0)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ['wifi', 'pool'])

    def test_update_and_save_place(self):
        """
        test_update_and_save_place tests that when a Place object is
        updated and saved the updated_at attribute is updated
        """
        place = Place()
        place.city_id = '123'
        place.user_id = '456'
        place.name = 'Test Place'
        place.description = 'This is a test place'
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100.0
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ['wifi', 'pool']
        place.save()

        self.assertEqual(place.city_id, '123')
        self.assertEqual(place.user_id, '456')
        self.assertEqual(place.name, 'Test Place')
        self.assertEqual(place.description, 'This is a test place')
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100.0)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ['wifi', 'pool'])

    #  Place object attributes can be accessed and modified
    def test_access_and_modify_attributes(self):
        place = Place()
        place.city_id = '123'
        place.user_id = '456'
        place.name = 'Test Place'
        place.description = 'This is a test place'
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100.0
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ['wifi', 'pool']

        self.assertEqual(place.city_id, '123')
        self.assertEqual(place.user_id, '456')
        self.assertEqual(place.name, 'Test Place')
        self.assertEqual(place.description, 'This is a test place')
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100.0)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ['wifi', 'pool'])

        place.city_id = '789'
        place.user_id = '012'
        place.name = 'Modified Place'
        place.description = 'This is a modified place'
        place.number_rooms = 3
        place.number_bathrooms = 2
        place.max_guest = 6
        place.price_by_night = 200.0
        place.latitude = 37.7748
        place.longitude = -122.4195
        place.amenity_ids = ['wifi', 'pool', 'gym']

        self.assertEqual(place.city_id, '789')
        self.assertEqual(place.user_id, '012')
        self.assertEqual(place.name, 'Modified Place')
        self.assertEqual(place.description, 'This is a modified place')
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 6)
        self.assertEqual(place.price_by_night, 200.0)
        self.assertEqual(place.latitude, 37.7748)
        self.assertEqual(place.longitude, -122.4195)
        self.assertEqual(place.amenity_ids, ['wifi', 'pool', 'gym'])

    def test_create_place_with_minimum_attributes(self):
        """
        test_create_place_with_minimum_attributes tests that
        when a Place object is
        """
        place = Place(city_id='123', user_id='456', name='Test Place')

        self.assertEqual(place.city_id, '123')
        self.assertEqual(place.user_id, '456')
        self.assertEqual(place.name, 'Test Place')
        self.assertEqual(place.description, '')
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_create_place_with_maximum_attributes(self):
        """
        test_create_place_with_maximum_attributes tests that when
        a Place object is
        """
        place = Place(city_id='123', user_id='456', name='Test Place',
                      description='This is a test place',
                      number_rooms=1000000, number_bathrooms=1000000,
                      max_guest=1000000, price_by_night=1000000.0,
                      latitude=90.0, longitude=180.0,
                      amenity_ids=['wifi'] * 1000000)

        self.assertEqual(place.city_id, '123')
        self.assertEqual(place.user_id, '456')
        self.assertEqual(place.name, 'Test Place')
        self.assertEqual(place.description, 'This is a test place')
        self.assertEqual(place.number_rooms, 1000000)
        self.assertEqual(place.number_bathrooms, 1000000)
        self.assertEqual(place.max_guest, 1000000)
        self.assertEqual(place.price_by_night, 1000000.0)
        self.assertEqual(place.latitude, 90.0)
        self.assertEqual(place.longitude, 180.0)
        self.assertEqual(place.amenity_ids, ['wifi'] * 1000000)

    def test_create_place_with_empty_string_attributes(self):
        """
        test_create_place_with_empty_string_attributes tests that
        when a Place object is
        """
        place = Place(city_id='', user_id='', name='', description='')

        self.assertEqual(place.city_id, '')
        self.assertEqual(place.user_id, '')
        self.assertEqual(place.name, '')
        self.assertEqual(place.description, '')
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_create_place_with_integer_values_for_float_attributes(self):
        """
        test_create_place_with_integer_values_for_float_attributes
        tests that when a Place
        """
        place = Place(price_by_night=100, latitude=37, longitude=-122)

        self.assertEqual(place.price_by_night, 100.0)
        self.assertEqual(place.latitude, 37.0)
        self.assertEqual(place.longitude, -122.0)

    def test_create_place_with_non_ascii_characters(self):
        """
        test_create_place_with_non_ascii_characters tests that
        when a Place object is
        """
        place = Place(name='Café')

        self.assertEqual(place.name, 'Café')

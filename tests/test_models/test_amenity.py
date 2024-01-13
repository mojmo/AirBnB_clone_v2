import unittest

from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_amenity_instance_with_name_attribute(self):
        """
        Test that an Amenity instance can be created with a name attribute
        """
        amenity = Amenity(name="Sw")
        self.assertEqual(amenity.name, "Sw")

    def test_amenity_instance_without_name_attribute(self):
        """
        Test that an Amenity instance can be created without a name attribute
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_instance_with_non_string_name_attribute(self):
        """
        Test that an Amenity instance can be created with a non-string name attribute
        """
        amenity = Amenity(name=123)
        self.assertEqual(amenity.name, 123)

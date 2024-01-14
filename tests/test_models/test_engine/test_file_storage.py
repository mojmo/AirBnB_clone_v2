"""Unit tests for the FileStorage class."""
import unittest
import os
from unittest.mock import patch

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.engine.file_storage import get_class_name_to_class


class TestFileStorage(unittest.TestCase):
    """Contains unit tests for the FileStorage class."""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_create_instance(self):
        """
        Test that a new instance of FileStorage can be created.
        """
        file_storage = FileStorage()
        self.assertIsInstance(file_storage, FileStorage)

    def test_all_method_returns_dict(self):
        """Tests that the 'all' method returns a dictionary."""
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_add_object(self):
        """
        Test that a new object can be added to the __objects
        dictionary using the new method.
        """
        file_storage = FileStorage()
        # Use an instance of a class derived from BaseModel
        obj = BaseModel()
        file_storage.new(obj)
        self.assertIn(obj, file_storage.all().values())

    def test_new_method_and_get_class_method(self):
        """Tests the 'new' method and 'get_class_name_to_class' function."""
        class_dict = get_class_name_to_class()
        all_objects = storage.all()
        obj = class_dict['User']()
        obj_name = f'{obj.__class__.__name__}.{obj.id}'
        storage.new(obj)
        self.assertIn(obj_name, all_objects)

    def test_new_method_for_state_class(self):
        """Tests the 'new' method for the State class."""
        class_dict = get_class_name_to_class()
        all_objects = storage.all()
        obj = class_dict['State']()
        obj_name = f'{obj.__class__.__name__}.{obj.id}'
        storage.new(obj)
        self.assertIn(obj_name, all_objects)

    def test_new_method_for_city_class(self):
        """Tests the 'new' method for the City class."""
        class_dict = get_class_name_to_class()
        all_objects = storage.all()
        obj = class_dict['City']()
        obj_name = f'{obj.__class__.__name__}.{obj.id}'
        storage.new(obj)
        self.assertIn(obj_name, all_objects)

    def test_new_method_for_amenity_class(self):
        """Tests the 'new' method for the Amenity class."""
        class_dict = get_class_name_to_class()
        all_objects = storage.all()
        obj = class_dict['Amenity']()
        obj_name = f'{obj.__class__.__name__}.{obj.id}'
        storage.new(obj)
        self.assertIn(obj_name, all_objects)

    def test_new_method_for_place_class(self):
        """Tests the 'new' method for the Place class."""
        class_dict = get_class_name_to_class()
        all_objects = storage.all()
        obj = class_dict['Place']()
        obj_name = f'{obj.__class__.__name__}.{obj.id}'
        storage.new(obj)
        self.assertIn(obj_name, all_objects)

    def test_new_method_for_review_class(self):
        """Tests the 'new' method for the Review class."""
        class_dict = get_class_name_to_class()
        all_objects = storage.all()
        obj = class_dict['Review']()
        obj_name = f'{obj.__class__.__name__}.{obj.id}'
        storage.new(obj)
        self.assertIn(obj_name, all_objects)

    def test_save_method_creates_json_file(self):
        """
        Tests that the 'save' method creates a JSON file
        with object information.
        """
        obj = BaseModel()
        obj_name = f'{obj.__class__.__name__}.{obj.id}'
        storage.new(obj)
        storage.save()

        with open("file.json", "r") as file:
            content = file.read()
            self.assertIn(obj_name, content)

    def test_reload_method_loads_objects(self):
        """Tests that the 'reload' method loads objects from the JSON file."""
        obj = BaseModel()
        file_storage = FileStorage()
        obj_name = f'{obj.__class__.__name__}.{obj.id}'
        file_storage.new(obj)
        file_storage.save()
        file_storage.reload()

        self.assertIn(obj_name, file_storage.all().keys())

    def test_all_method_with_arg(self):
        """Tests that the 'all' method raises a TypeError with an argument."""
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_save_method_with_arg(self):
        """Tests that the 'save' method raises a TypeError with an argument."""
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload_method_with_arg(self):
        """
        Tests that the 'reload' method raises
        a TypeError with an argument.
        """
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_new_method_with_two_args(self):
        """
        Tests that the 'new' method raises
        a TypeError with two arguments.
        """
        obj = BaseModel
        with self.assertRaises(TypeError):
            storage.new(obj, None)

    def test_reload_file_not_found(self):
        """
        Tests that the 'reload' method handles
        FileNotFound error gracefully.
        """
        # No exception should be raised,
        # and the method should return without errors
        with patch('builtins.open', side_effect=FileNotFoundError()):
            storage.reload()

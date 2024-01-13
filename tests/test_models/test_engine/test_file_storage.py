import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def test_create_instance(self):
        """
        Test that a new instance of FileStorage can be created.
        """
        file_storage = FileStorage()
        self.assertIsInstance(file_storage, FileStorage)

    def test_add_object(self):
        """
        Test that a new object can be added to the __objects dictionary using the new method.
        """
        file_storage = FileStorage()
        # Use an instance of a class derived from BaseModel
        obj = BaseModel()
        file_storage.new(obj)
        self.assertIn(obj, file_storage.all().values())

    def test_reload_objects(self):
        """
        Test that the __objects dictionary can be reloaded from a file using the reload method.
        """
        file_storage = FileStorage()
        obj = BaseModel()
        file_storage.new(obj)
        file_storage.save()
        file_storage.reload()

        self.assertIn(obj, file_storage.all().values())

#!/usr/bin/python3
"""Provides a simple storage system for managing and persisting
objects in JSON format."""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Handles the storage and retrieval of objects in JSON format."""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Retrieve all stored objects.

        Returns:
            dict: A dictionary containing all stored objects.
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to the storage.

        Args:
            obj: An object to be stored.
        """
        obj_name = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[obj_name] = obj

    def save(self):
        """Save the current state of stored objects to the JSON file."""

        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """Load objects from the JSON file into the storage dictionary."""

        try:
            with open(FileStorage.__file_path) as json_file:
                objects_dict = json.load(json_file)

                for obj in objects_dict.values():
                    class_name = obj['__class__']
                    self.new(eval(class_name)(**obj))

        except FileNotFoundError:
            return

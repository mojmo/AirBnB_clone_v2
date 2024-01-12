#!/usr/bin/python3
""""""
import json
from models.base_model import BaseModel


class FileStorage:
    """"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """"""

        return FileStorage.__objects

    def new(self, obj):
        """"""
        obj_name = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[obj_name] = obj

    def save(self):
        """"""

        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """"""

        try:
            with open(FileStorage.__file_path) as json_file:
                objects_dict = json.load(json_file)

                for obj in objects_dict.values():
                    class_name = obj['__class__']
                    self.new(eval(class_name)(**obj))

        except FileNotFoundError:
            return

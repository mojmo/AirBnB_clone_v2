#!/usr/bin/python3
""""""
import json


def get_class_name_to_class():
    # This function is used to avoid circular import
    from models.user import User
    from models.state import State
    from models.city import City
    from models.amenity import Amenity
    from models.place import Place
    from models.review import Review

    return {
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }


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
        class_name_to_class = get_class_name_to_class()

        try:
            with open(FileStorage.__file_path) as json_file:
                objects_dict = json.load(json_file)

                for obj in objects_dict.values():
                    class_name = obj['__class__']
                    # Use the mapping insted of eval function
                    # to avoid security issues with eval function
                    if class_name in class_name_to_class:
                        cls = class_name_to_class[class_name]
                        # self.new(eval(class_name)(**obj))
                        self.new(cls(**obj))

        except FileNotFoundError:
            return
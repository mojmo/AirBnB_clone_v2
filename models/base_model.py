#!/usr/bin/python3
""""""
from datetime import datetime
from uuid import uuid4

import models


class BaseModel:
    """"""

    def __init__(self, *args, **kwargs):
        """"""
        if kwargs:
            # The __class__ key if being deleted from the kwargs
            # in the BaseModel __init__ method without first checking if it exists.
            # it will throw a KeyError if the key is not present in the kwargs.
            # we should only delete it if it's actually present in the kwargs.
            # so we use the pop method instead of the del method.
            kwargs.pop('__class__', None)
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    setattr(self,
                            key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """"""

        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()

        return new_dict

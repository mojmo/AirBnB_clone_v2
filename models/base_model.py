#!/usr/bin/python3
"""Provides a base class for data models with common functionality."""
from datetime import datetime
from uuid import uuid4

import models


class BaseModel:
    """Base class for data models."""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
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
        """
        Return a string representation of the object.

        Returns:
            str: String representation of the object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save the current state of the object and trigger
        the storage save process.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Convert the object to a dictionary format for storage.

        Returns:
            dict: Dictionary representation of the object.
        """

        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()

        return new_dict

#!/usr/bin/python3
""" Defines the Amenity class as a subclass of BaseModel."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity entity."""

    name = ''

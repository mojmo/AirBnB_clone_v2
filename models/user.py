#!/usr/bin/python3
"""Defines the User class as a subclass of BaseModel."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user entity."""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

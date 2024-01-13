#!/usr/bin/python3
"""Defines the City class as a subclass of BaseModel."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city entity."""

    state_id = ''
    name = ''

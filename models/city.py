#!/usr/bin/python3
"""Defines the City class as a subclass of BaseModel."""
from sqlalchemy import Column, String, ForeignKey

from models import storage_type
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """Represents a city entity."""

    if storage_type == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        name = ''
        state_id = ''

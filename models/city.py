#!/usr/bin/python3
"""Defines the City class as a subclass of BaseModel."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """Represents a city entity."""

    __tablename__ = 'cities'
    name =  Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

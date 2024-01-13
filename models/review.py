#!/usr/bin/python3
"""Defines the Review class as a subclass of BaseModel."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review entity."""

    place_id = ''
    user_id = ''
    text = ''

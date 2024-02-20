#!/usr/bin/python3
"""Defines the State class as a subclass of BaseModel."""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage, storage_type

class State(BaseModel, Base):
    """Represents a state entity."""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if storage_type is not 'db':
        @property
        def cities(self):
            """Return a list of City instances associated with this State.

            Returns:
                list: A list of City instances that have the same
                state_id as this State's id.
            """
            cities_list = []
            
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list

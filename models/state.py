#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    if storage_type == "db"
    name = Column(String(128),
                  nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """Returns a list of city instances"""
            city_list = []
            city_all = models.storage.all(City)
            for city in city_all.values():
                if city.state.id == self.id:
                    city_list.append(city)
            return city_list

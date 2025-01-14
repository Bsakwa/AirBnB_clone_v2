#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'amenities'
        name = Column(String(128),
                      nullable=False)
        place_amenities = relationship('Place', secondary='place_amenity',
                                       viewonly=False,)

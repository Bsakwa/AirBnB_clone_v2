#!/usr/bin/python3
""" holds class Amenity"""
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity:
    """Instantiates a new Amenity"""
    name = ''

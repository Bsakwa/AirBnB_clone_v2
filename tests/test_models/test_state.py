#!/usr/bin/python3
"""Defines Unittests for models/state.py """

import os
import pycodestyle
import models
import MySQLdb
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.engine.file_storage import FileStorage
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker


class TestState(unittest.TestCase):
    """Unittests for testing the State class."""

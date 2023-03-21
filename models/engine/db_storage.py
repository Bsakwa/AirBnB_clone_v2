#!/usr/bin/python3
"""Defines the new database storage for our models"""
from os import getenv
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage():
    """Defines our hbnb_dev_db"""
    #Private class attributes
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the new database"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('localhost')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.engine)

    def all(self, cls=None):
        """Query the Database Session"""
        all_dict = {}
        for i in classes:
            if cls is None or cls == i:
                objs = self.__session.query(classes[i]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    all_dict[key] = obj
        return (all_dict)

    def new(self, obj):
        """Add a new object to the database"""
        if obj is not None:
            self.__session.add(obj)
            self.save()

    def save(self):
        """Saves the changes made to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj if exists"""
        if obj is not None:
            del obj
            self.save()

    def reload(self):
        """Creates all the tables from the database"""
        Base.metadata.create_all(self.__engine)
        cur = sessionmaker(
                            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(cur)
        self.session = Session()

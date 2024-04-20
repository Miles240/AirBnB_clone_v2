#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import datetime
from models import storage
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String, unique=True, primary_key=True, nullable=False)
    created_at = Column(DateTime, default=(datetime.utcnow()), nullable=False)
    updated_at = Column(DateTime, default=(datetime.utcnow()), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialization of the BaseModel class
        Args:
                - *args: list of arguements
                - **kwargs: key/value pair arguements
        """
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.datetime.now()
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """returns the string representation of an instance"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """returns the dictionary representation of the Base class"""
        dict_class = self.__dict__.copy()
        dict_class["__class__"] = type(self).__name__
        dict_class["created_at"] = dict_class["created_at"].isoformat()
        dict_class["updated_at"] = dict_class["updated_at"].isoformat()
        if "_sa_instance_state" in dict_class.keys():
            del dict_class["_sa_instance_state"]
        return dict_class

    def delete(self):
        """delete the current instance from the storage"""
        storage.delete(self)

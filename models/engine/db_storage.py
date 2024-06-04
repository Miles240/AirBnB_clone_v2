#!/usr/bin/python3

"""Module for DBStorage"""

import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):

        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, password, host, database),
            pool_pre_ping=True,
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session:
            - if cls=None, query all types of objects
            - return a dictionary
        """
        dic = {}
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            query = self.__session.query(cls).all()
            for obj in query:
                key = f"{type(obj).__name__}.{obj.id}"
                dic[key] = obj
        else:
            cls_list = [Amenity, City, Place, Review, State, User]

            for clas in cls_list:
                query = self.__session.query(clas).all()
                for obj in query:
                    key = f"{type(obj).__name__}.{obj.id}"
                    dic[key] = obj
        return dic

    def new(self, obj):
        """adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        # Base.metadata.drop_all(bind=self.__engine)
        Base.metadata.create_all(bind=self.__engine)
        session_fac = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fac)
        self.__session = Session()

    def close(self):
        """Closes the cuurent session"""
        self.__session.close()

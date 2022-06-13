#!/usr/bin/python3
""" This file manage all the database """

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from models.base_model import Base
from models.department import Department
from models.city import City
from models.user import User
from models.sport import Sport
"""from models.event import Event"""
"""from models.review import Review"""
import models


class DBStorage:
    """ this class will contain all the manages of database
    """

    __engine = None
    __session = None

    def __init__(self):
        """ this contain the definition of environ variables
            the creation of engine and the reload that if
            the test is equal to the environment should drop
            down all the tables.
        """

        my_user = "motiv_dev"
        my_psswd = "motiv"
        my_host = "localhost"
        my_datab = "motiv_dev_db"

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(my_user, my_psswd,
                                              my_host, my_datab),
                                      pool_pre_ping=True)
        self.reload()


    def all(self, cls=None):
        """ this contain the filter that depend of the class
            that is specified
        """
        dicti = {}
        list_cls = []

        if cls is None:
            list_cls += self.__session.query(Department).all()
            list_cls += self.__session.query(City).all()
            list_cls += self.__session.query(User).all()
            list_cls += self.__session.query(Event).all()
            list_cls += self.__session.query(Review).all()
            list_cls += self.__session.query(Sport).all()

        else:
            list_cls = self.__session.query(cls).all()

        for var in list_cls:
            k = type(var).__name__ + '.' + var.id
            dicti[k] = var

        return dicti

    def new(self, obj):
        """ add the object to session """

        self.__session.add(obj)

    def save(self):
        """ commit all the changes to session """

        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the session """

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ This function create all the tables and the session """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))()

    def get(self, cls, id):
        """ Method to retrieve one object:. """
        all_obj = models.storage.all(cls)

        for k, v in all_obj.items():
            if v.id == id:
                return v
        return None

    def count(self, cls=None):
        """ Methode to count the number of objects in storage. """
        if cls is None:
            return len(models.storage.all())
        return len(models.storage.all(cls))

    def close(self):
        """ This function close engines"""
        self.__session.close()

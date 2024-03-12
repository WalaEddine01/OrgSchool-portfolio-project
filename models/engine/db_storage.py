#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.base_model import BaseModel, Base
from models.student import Student
from models.school import School
from models.teacher import Teacher
from models.sclass import SClass
from models.admin import Admin
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Student": Student,"School": School, "Teacher": Teacher,
           "SClass": SClass, "Admin": Admin}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        ORG_MYSQL_USER = "org_dev"
        ORG_MYSQL_PWD = "org_dev_pwd"
        ORG_MYSQL_HOST = "localhost"
        ORG_MYSQL_DB = "org_dev_db"
        ORG_ENV = getenv('ORG_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(ORG_MYSQL_USER,
                                             ORG_MYSQL_PWD,
                                             ORG_MYSQL_HOST,
                                             ORG_MYSQL_DB))
        if ORG_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        if cls:
            for obj in self.__session.query(cls):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                new_dict[key] = obj
        else:
            for clas in classes.values():
                for obj in self.__session.query(clas):
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None
    
    def get_by_key(self, cls, key, value):
        """
        Returns the object based on the key, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)

        for obj in all_cls.values():
            if (getattr(obj, key) == value):
                return obj

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count
    
    def get_session(self):
        """ return the session """
        return self.__session

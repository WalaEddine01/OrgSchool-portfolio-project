#!/usr/bin/python
""" holds class Student"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Student(BaseModel, Base):
    """Representation of student """
    if models.storage_t == "db":
        __tablename__ = 'cities'
        class_id = Column(String(60), ForeignKey('classs.id'), nullable=False)
        name = Column(String(128), nullable=False)
        schools = relationship("Place",
                              backref="cities",
                              cascade="all, delete, delete-orphan")
    else:
        class_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes student"""
        super().__init__(*args, **kwargs)

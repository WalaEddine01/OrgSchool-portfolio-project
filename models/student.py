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
    if models.storage_t == 'db':
        __tablename__ = 'students'
        name = Column(String(128), nullable=False)
        sclass_id = Column(String(60), ForeignKey('sclasses.id'), nullable=False)
    else:
        name = ""


    def __init__(self, *args, **kwargs):
        """initializes student"""
        super().__init__(*args, **kwargs)

#!/usr/bin/python
""" holds class Teacher"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Teacher(BaseModel, Base):
    """Representation of Teacher """
    if models.storage_t == 'db':
        __tablename__ = 'teachers'
        name = Column(String(128), nullable=False)
        school_id = Column(String(60), ForeignKey('schools.id'), nullable=False)

    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Teacher"""
        super().__init__(*args, **kwargs)

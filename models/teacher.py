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
        school_id = Column(String(60), ForeignKey('schools.id'), nullable=False)
        admin_id = Column(String(60), ForeignKey('admins.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        school_id = ""
        admin_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Teacher"""
        super().__init__(*args, **kwargs)

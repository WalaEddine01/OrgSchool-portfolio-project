#!/usr/bin/python
""" holds class Student"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Student(BaseModel, Base):
    """Representation of student """
    if models.storage_t == 'db':
        __tablename__ = 'students'
        name = Column(String(128), nullable=False)
        age = Column(Integer, nullable=False)
        sclass_id = Column(String(60), ForeignKey('sclasses.id'), nullable=False)
        admin_id = Column(String(60), ForeignKey('admins.id'), nullable=False)
        admin = relationship('Admin', back_populates="students")
        sclass = relationship("SClass", back_populates="students")
    else:
        name = ""
        age = 0
        sclass_id = ""


    def __init__(self, *args, **kwargs):
        """initializes student"""
        super().__init__(*args, **kwargs)
    
    if models.storage_t != 'db':
        @property
        def sclass(self):
            """getter attribute that links with sclass"""
            from models.sclass import SClass
            sclass = models.storage.get('SClass', self.sclass_id)
            return sclass
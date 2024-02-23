#!/usr/bin/python
""" holds class School"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class School(BaseModel, Base):
    """Representation of School """
    if models.storage_t == 'db':
        __tablename__ = 'schools'
        sclass_id = Column(String(60), ForeignKey('sclasses.id'), nullable=False)
        admin_id = Column(String(60), ForeignKey('admins.id'), nullable=False)
        name = Column(String(128), nullable=False)
        
    else:
        name = ""


    def __init__(self, *args, **kwargs):
        """initializes School"""
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        @property
        def sclasses(self):
            """getter attribute that links with sclasses"""
            list_sclasses = []
            all_sclasses = models.storage.all('Sclass')
            for sclass in all_sclasses.values():
                if sclass.school_id == self.id:
                    list_sclasses.append(sclass)
            return list_sclasses

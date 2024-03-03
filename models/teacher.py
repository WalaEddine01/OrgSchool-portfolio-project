#!/usr/bin/python
""" holds class Teacher"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Teacher(BaseModel, Base):
    """Representation of Teacher """
    if models.storage_t == 'db':
        __tablename__ = 'teachers'
        name = Column(String(128), nullable=False)
        sclass_id = Column(String(60), ForeignKey('sclasses.id'), nullable=False)
        admin_id = Column(String(60), ForeignKey('admins.id'), nullable=False)
        admin = relationship('Admin', back_populates="teachers")
        sclass = relationship("SClass", back_populates="teachers")


    else:
        name = ""
        sclass_id = ""

    def __init__(self, *args, **kwargs):
        """initializes Teacher"""
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        @property
        def sclass(self):
            """getter attribute that links with sclass"""
            from models.sclass import SClass
            sclass = models.storage.get('SClass', self.sclass_id)
            return sclass
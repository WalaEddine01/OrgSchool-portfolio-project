#!/usr/bin/python3
""" holds class admin"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class Admin(BaseModel, Base):
    """Representation of a admin """
    if models.storage_t == 'db':
        __tablename__ = 'admins'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        username = Column(String(128), nullable=False)
        schools = relationship("School", back_populates="admin")

    else:
        email = ""
        password = ""
        username = ""

    def __init__(self, *args, **kwargs):
        """initializes admin"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
    
    if models.storage_t != 'db':
        @property
        def schools(self):
            """getter attribute that links with schools"""
            list_schools = []
            all_schools = models.storage.all('School')
            for school in all_schools.values():
                if school.admin_id == self.id:
                    list_schools.append(school)
            return list_schools

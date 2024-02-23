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

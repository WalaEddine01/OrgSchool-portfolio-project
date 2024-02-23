#!/usr/bin/python3
""" holds class SClass"""
import models
from models.base_model import BaseModel, Base
from models.student import Student
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class SClass(BaseModel, Base):
    """Representation of sclass """
    if models.storage_t == "db":
        __tablename__ = 'sclasses'
        name = Column(String(128), nullable=False)
        school_id = Column(String(60), ForeignKey('schools.id'), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes sclass"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def students(self):
            """getter attribute that links with students"""
            list_students = []
            all_students = models.storage.all('Student')
            for student in all_students.values():
                if student.sclass_id == self.id:
                    list_students.append(student)
            return list_students

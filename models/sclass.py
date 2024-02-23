#!/usr/bin/python3
""" holds class Class"""
import models
from models.base_model import BaseModel, Base
from models.student import Student
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class SClass(BaseModel, Base):
    """Representation of sclass """
    if models.storage_t == "db":
        __tablename__ = 'sclasses'
        name = Column(String(128), nullable=False)
        cities = relationship("Student",
                              backref="sclass",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes sclass"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """getter for list of student instances related to the sclass"""
            student_list = []
            all_cities = models.storage.all(Student)
            for student in all_cities.values():
                if student.class_id == self.id:
                    student_list.append(student)
            return student_list

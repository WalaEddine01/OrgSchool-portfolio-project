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
        student_id = Column(String(60), ForeignKey('students.id'), nullable=False)
        admin_id = Column(String(60), ForeignKey('admins.id'), nullable=False)
        number = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        teachers = relationship("Teacher",
                               backref="school",
                               cascade="all, delete, delete-orphan")
    else:
        student_id = ""
        admin_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes School"""
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        @property
        def teachers(self):
            """getter attribute returns the list of Teacher instances"""
            from models.teacher import Teacher
            teacher_list = []
            all_teachers = models.storage.all(Teacher)
            for teacher in all_teachers.values():
                if teacher.school_id == self.id:
                    teacher_list.append(teacher)
            return teacher_list


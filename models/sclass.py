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
        school = relationship("School", back_populates="sclasses")
        students = relationship("Student", back_populates="sclass")
        teachers = relationship("Teacher", back_populates="sclass")

    else:
        name = ""
        school_id = ""

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

        @property
        def teachers(self):
            """getter attribute that links with teachers"""
            list_teachers = []
            all_teachers = models.storage.all('Teacher')
            for teacher in all_teachers.values():
                if teacher.sclass_id == self.id:
                    list_teachers.append(teacher)
            return list_teachers
        
        @property
        def school(self):
            """getter attribute that links with school"""
            from models.school import School
            school = models.storage.get('School', self.school_id)
            return school

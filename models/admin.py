#!/usr/bin/python3
""" holds class admin"""
from time import sleep
import models
from models.base_model import BaseModel, Base
from models.school import School
from models.sclass import SClass
from sqlalchemy import Column, String, event
from sqlalchemy.orm import relationship
from hashlib import md5


class Admin(BaseModel, Base):
    """Representation of a admin """
    if models.storage_t == 'db':
        __tablename__ = 'admins'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        school_name = Column(String(128), nullable=False)
        schools = relationship("School", back_populates="admin")

    else:
        email = ""
        password = ""
        school_name = ""

    def __init__(self, *args, **kwargs):
        """initializes admin"""
        super().__init__(*args, **kwargs)
        if models.storage_t != 'db':
            self.create_school_and_4_sclasses()

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

    def create_school_and_4_sclasses(self):
        """Creates a school and 4 sclasses after an admin is created"""
        new_school = School(admin_id=self.id, name=self.school_name)
        for i in range(4):
            new_sclass = SClass(school_id=new_school.id, name="SClass " + str(i + 1))
        models.storage.save()

if models.storage_t == 'db':
    @event.listens_for(Admin, 'after_insert')
    def create_school(mapper, connection, target):
        """Creates a school and 4 sclasses after an admin is created"""
        new_school = School(admin_id=target.id, name=target.school_name)
        models.storage.new(new_school)
        for i in range(4):
            new_sclass = SClass(school_id=new_school.id, name="SClass " + str(i + 1))
            models.storage.new(new_sclass)

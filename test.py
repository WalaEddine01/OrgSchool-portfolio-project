#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.student import Student

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(Student)))

first_state_id = list(storage.all(Student).values())[0].id
print("First state: {}".format(storage.get(Student, first_state_id)))

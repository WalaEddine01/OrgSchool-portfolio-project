#!/usr/bin/python3
""" Index """
from models.amenity import Amenity
from models.student import Student
from models.class import Place
from models.teacher import Teacher
from models.class import Class
from models.admin import Admin
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [Amenity, Student, Place, Teacher, Class, Admin]
    names = ["amenities", "cities", "schools", "teachers", "classs", "admins"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)

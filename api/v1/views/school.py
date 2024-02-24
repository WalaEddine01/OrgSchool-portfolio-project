#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Places """
from models.sclass import SClass
from models.student import Student
from models.school import School
from models.admin import Admin
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/schools', methods=['GET'], strict_slashes=False)
@swag_from('documentation/school/all_schools.yml')
def get_schools():
    """
    Retrieves the list of all school objects
    or a specific school
    """
    schools = storage.all(School).values()
    schools = [school.to_dict() for school in schools]
    return jsonify(schools)

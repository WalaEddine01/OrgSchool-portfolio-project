#!/usr/bin/python3
""" objects that handles all default RestFul API actions for cities """
from models.student import Student
from models.class import Class
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/classs/<class_id>/cities', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/student/cities_by_class.yml', methods=['GET'])
def get_cities(class_id):
    """
    Retrieves the list of all cities objects
    of a specific Class, or a specific student
    """
    list_cities = []
    class = storage.get(Class, class_id)
    if not class:
        abort(404)
    for student in class.cities:
        list_cities.append(student.to_dict())

    return jsonify(list_cities)


@app_views.route('/cities/<student_id>/', methods=['GET'], strict_slashes=False)
@swag_from('documentation/student/get_student.yml', methods=['GET'])
def get_student(student_id):
    """
    Retrieves a specific student based on id
    """
    student = storage.get(Student, student_id)
    if not student:
        abort(404)
    return jsonify(student.to_dict())


@app_views.route('/cities/<student_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/student/delete_student.yml', methods=['DELETE'])
def delete_student(student_id):
    """
    Deletes a student based on id provided
    """
    student = storage.get(Student, student_id)

    if not student:
        abort(404)
    storage.delete(student)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/classs/<class_id>/cities', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/student/post_student.yml', methods=['POST'])
def post_student(class_id):
    """
    Creates a Student
    """
    class = storage.get(Class, class_id)
    if not class:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Student(**data)
    instance.class_id = class.id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/cities/<student_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/student/put_student.yml', methods=['PUT'])
def put_student(student_id):
    """
    Updates a Student
    """
    student = storage.get(Student, student_id)
    if not student:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'class_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(student, key, value)
    storage.save()
    return make_response(jsonify(student.to_dict()), 200)

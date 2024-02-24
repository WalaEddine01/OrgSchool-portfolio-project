#!/usr/bin/python3
""" objects that handles all default RestFul API actions for students """
from models.student import Student
from models.sclass import SClass
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/sclasses/<sclass_id>/students', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/student/get_students.yml', methods=['GET'])
def get_cities(sclass_id):
    """
    Retrieves the list of all student objects
    of a specific SClass, or a specific student
    """
    sclass = storage.get(SClass, sclass_id)
    if not sclass:
        abort(404)
    list_students = []
    for student in sclass.students:
        list_students.append(student.to_dict())
    return jsonify(list_students)


@app_views.route('/students/<student_id>/', methods=['GET'], strict_slashes=False)
@swag_from('documentation/student/get_student.yml', methods=['GET'])
def get_student(student_id):
    """
    Retrieves a specific student based on id
    """
    student = storage.get(Student, student_id)
    if not student:
        abort(404)
    return jsonify(student.to_dict())


@app_views.route('/students/<student_id>', methods=['DELETE'], strict_slashes=False)
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


@app_views.route('/sclasses/<sclass_id>/students', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/student/post_student.yml', methods=['POST'])
def post_student(sclass_id):
    """
    Creates a Student
    """
    sclass = storage.get(SClass, sclass_id)
    if not sclass:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    if 'age' not in request.get_json() or type(request.get_json()['age']) is not int:
        abort(400, description="Missing age")

    data = request.get_json()
    data['sclass_id'] = sclass_id
    instance = Student(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/students/<student_id>', methods=['PUT'], strict_slashes=False)
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

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
@swag_from('documentation/student/all_students.yml', methods=['GET'])
def get_cities(sclass_id):
    """ Retrieves the list of all students of a class """
    sclass = storage.get(SClass, sclass_id)
    if sclass is None:
        abort(404)
    students = [student.to_dict() for student in sclass.students]
    return jsonify(students)

@app_views.route('/sclasses/<sclass_id>/students/<student_id>', methods=['GET'],
                    strict_slashes=False)
@swag_from('documentation/student/get_student.yml', methods=['GET'])
def get_student(sclass_id, student_id):
    """ Retrieves a student """
    student = storage.get(Student, student_id)
    if student is None:
        abort(404)
    return jsonify(student.to_dict())

@app_views.route('/sclasses/<sclass_id>/students', methods=['POST'],
                    strict_slashes=False)
@swag_from('documentation/student/post_student.yml', methods=['POST'])
def post_student(sclass_id):
    """ Creates a student """
    sclass = storage.get(SClass, sclass_id)
    if sclass is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 400)
    if 'age' not in request.get_json():
        return make_response(jsonify({'error': 'Missing age'}), 400)
    student = Student(**request.get_json())
    student.sclass_id = sclass_id
    student.save()
    return make_response(jsonify(student.to_dict()), 201)

@app_views.route('/sclasses/<sclass_id>/students/<student_id>', methods=['DELETE'],
                    strict_slashes=False)
@swag_from('documentation/student/delete_student.yml', methods=['DELETE'])
def delete_student(sclass_id, student_id):
    """ Deletes a student """
    student = storage.get(Student, student_id)
    if student is None:
        abort(404)
    student.delete()
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/sclasses/<sclass_id>/students/<student_id>', methods=['PUT'],
                    strict_slashes=False)
@swag_from('documentation/student/put_student.yml', methods=['PUT'])
def put_student(sclass_id, student_id):
    """ Updates a student """
    student = storage.get(Student, student_id)
    if student is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(student, key, value)
    student.save()
    return make_response(jsonify(student.to_dict()), 200)

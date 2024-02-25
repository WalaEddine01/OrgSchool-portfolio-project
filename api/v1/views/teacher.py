#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Teachers """
from models.teacher import Teacher
from models.sclass import SClass
from models.admin import Admin
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/sclasses/<sclass_id>/teachers', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/teacher/all_teachers.yml', methods=['GET'])
def get_teachers(sclass_id):
    """ Retrieves the list of all teachers of a class """
    sclass = storage.get(SClass, sclass_id)
    if sclass is None:
        abort(404)
    teachers = [teacher.to_dict() for teacher in sclass.teachers]
    return jsonify(teachers)

@app_views.route('/sclasses/<sclass_id>/teachers/<teacher_id>', methods=['GET'],
                    strict_slashes=False)
@swag_from('documentation/teacher/get_teacher.yml', methods=['GET'])
def get_teacher(sclass_id, teacher_id):
    """ Retrieves a teacher """
    sclass = storage.get(SClass, sclass_id)
    if sclass is None:
        abort(404)
    teacher = storage.get(Teacher, teacher_id)
    if teacher is None:
        abort(404)
    return jsonify(teacher.to_dict())

@app_views.route('/sclasses/<sclass_id>/teachers', methods=['POST'],
                    strict_slashes=False)
@swag_from('documentation/teacher/post_teacher.yml', methods=['POST'])
def post_teacher(sclass_id):
    """ Creates a teacher """
    sclass = storage.get(SClass, sclass_id)
    if sclass is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 400)
    teacher = Teacher(**request.get_json())
    teacher.sclass_id = sclass_id
    teacher.save()
    return make_response(jsonify(teacher.to_dict()), 201)

@app_views.route('/sclasses/<sclass_id>/teachers/<teacher_id>', methods=['DELETE'],
                    strict_slashes=False)
@swag_from('documentation/teacher/delete_teacher.yml', methods=['DELETE'])
def delete_teacher(sclass_id, teacher_id):
    """ Deletes a teacher """
    teacher = storage.get(Teacher, teacher_id)
    if teacher is None:
        abort(404)
    teacher.delete()
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/sclasses/<sclass_id>/teachers/<teacher_id>', methods=['PUT'],
                    strict_slashes=False)
@swag_from('documentation/teacher/put_teacher.yml', methods=['PUT'])
def put_teacher(sclass_id, teacher_id):
    """ Updates a teacher """
    teacher = storage.get(Teacher, teacher_id)
    if teacher is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(teacher, key, value)
    teacher.save()
    return make_response(jsonify(teacher.to_dict()), 200)
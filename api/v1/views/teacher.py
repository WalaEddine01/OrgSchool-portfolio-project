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
@swag_from('documentation/teachers/get_teachers.yml', methods=['GET'])
def get_teachers(sclass_id):
    """
    Retrieves the list of all Teacher objects of a Place
    """
    sclass = storage.get(SClass, sclass_id)
    if not sclass:
        abort(404)

    teachers = []
    for teacher in sclass.teachers:
        teachers.append(teacher.to_dict())

    return jsonify(teachers)


@app_views.route('/teachers/<teacher_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/teachers/get_teacher.yml', methods=['GET'])
def get_teacher(teacher_id):
    """
    Retrieves a Teacher object
    """
    teacher = storage.get(Teacher, teacher_id)
    if not teacher:
        abort(404)

    return jsonify(teacher.to_dict())


@app_views.route('/teachers/<teacher_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/teachers/delete_teachers.yml', methods=['DELETE'])
def delete_teacher(teacher_id):
    """
    Deletes a Teacher Object
    """

    teacher = storage.get(Teacher, teacher_id)

    if not teacher:
        abort(404)

    storage.delete(teacher)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/sclasses/<sclass_id>/teachers', methods=['POST'],
                    strict_slashes=False)
@swag_from('documentation/teachers/post_teachers.yml', methods=['POST'])
def post_teacher(sclass_id):
    """
    Creates a Teacher
    """
    sclass = storage.get(SClass, sclass_id)

    if not sclass:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    data['sclass_id'] = sclass_id
    instance = Teacher(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/teachers/<teacher_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/teachers/put_teachers.yml', methods=['PUT'])
def put_teacher(teacher_id):
    """
    Updates a Teacher
    """
    teacher = storage.get(Teacher, teacher_id)

    if not teacher:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at', 'sclass_id']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(teacher, key, value)
    storage.save()
    return make_response(jsonify(teacher.to_dict()), 200)

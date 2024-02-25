#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Places """
from models.school import School
from models.admin import Admin
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/schools', methods=['GET'], strict_slashes=False)
@swag_from('documentation/school/all_schools.yml', methods=['GET'])
def get_schools():
    """
    Retrieves the list of all school objects
    or a specific school
    """
    schools = storage.all(School).values()
    schools = [school.to_dict() for school in schools]
    return jsonify(schools)

@app_views.route('/schools/<school_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/school/get_school.yml', methods=['GET'])
def get_school(school_id):
    """
    Retrieves a specific school
    """
    school = storage.get(School, school_id)
    if school is None:
        abort(404)
    return jsonify(school.to_dict())

@app_views.route('/admins/<admin_id>/schools', methods=['POST'], strict_slashes=False)
@swag_from('documentation/school/post_school.yml', methods=['POST'])
def post_school(admin_id):
    """
    Creates a school
    """
    admin = storage.get(Admin, admin_id)
    if admin is None:
        abort(404)
    data = request.get_json()
    if data is None:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in data:
        return make_response(jsonify({'error': 'Missing name'}), 400)
    school = School(**data)
    school.admin_id = admin_id
    storage.new(school)
    storage.save()
    return make_response(jsonify(school.to_dict()), 201)


@app_views.route('/schools/<school_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/school/delete_school.yml', methods=['DELETE'])
def delete_school(school_id):
    """
    Deletes a school
    """
    school = storage.get(School, school_id)
    if school is None:
        abort(404)
    storage.delete(school)
    storage.save()
    return jsonify({}), 200

@app_views.route('/schools/<school_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/school/put_school.yml', methods=['PUT'])
def put_school(school_id):
    """
    Updates a school
    """
    school = storage.get(School, school_id)
    if school is None:
        abort(404)
    data = request.get_json()
    if data is None:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at', 'admin_id']:
            setattr(school, key, value)
    storage.save()
    return jsonify(school.to_dict()), 200


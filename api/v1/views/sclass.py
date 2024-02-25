#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Classs """
from models.sclass import SClass
from models.school import School
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/schools/<school_id>/sclasses', methods=['GET'],
                    strict_slashes=False)
@swag_from('documentation/sclass/all_sclasses.yml', methods=['GET'])
def get_classes(school_id):
    """ Retrieves the list of all Classs of a School """
    school = storage.get(School, school_id)
    if school is None:
        abort(404)
    classes = [sclass.to_dict() for sclass in school.sclasses]
    return jsonify(classes)

@app_views.route('/schools/<school_id>/sclasses/<sclass_id>', methods=['GET'],
                    strict_slashes=False)
@swag_from('documentation/sclass/get_sclass.yml', methods=['GET'])
def get_class(school_id, sclass_id):
    """ Retrieves a Class """
    school = storage.get(School, school_id)
    if school is None:
        abort(404)
    sclass = storage.get(SClass, sclass_id)
    if sclass is None or sclass not in school.sclasses:
        abort(404)
    return jsonify(sclass.to_dict())

@app_views.route('/schools/<school_id>/sclasses/<sclass_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/sclass/delete_sclass.yml', methods=['DELETE'])
def delete_class(school_id, sclass_id):
    """
    Deletes a Class Object
    """
    school = storage.get(School, school_id)
    if school is None:
        abort(404)
    sclass = storage.get(SClass, sclass_id)
    if sclass is None or sclass not in school.sclasses:
        abort(404)
    storage.delete(sclass)
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/schools/<school_id>/sclasses', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/sclass/post_sclass.yml', methods=['POST'])
def post_class(school_id):
    """
    Creates a Class
    """
    school = storage.get(School, school_id)
    if school is None:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    data = request.get_json()
    name = data['name']
    sclass = SClass(name=name)
    sclass.school = school
    storage.new(sclass)
    storage.save()
    return make_response(jsonify(sclass.to_dict()), 201)

@app_views.route('/schools/<school_id>/sclasses/<sclass_id>', methods=['PUT'],
                    strict_slashes=False)
@swag_from('documentation/sclass/put_sclass.yml', methods=['PUT'])
def put_class(school_id, sclass_id):
    """
    Updates a Class
    """
    school = storage.get(School, school_id)
    if school is None:
        abort(404)
    sclass = storage.get(SClass, sclass_id)
    if sclass is None or sclass not in school.sclasses:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(sclass, key, value)
    storage.save()
    return make_response(jsonify(sclass.to_dict()), 200)


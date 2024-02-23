#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Classs """
from models.class import Class
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/classs', methods=['GET'], strict_slashes=False)
@swag_from('documentation/class/get_class.yml', methods=['GET'])
def get_classs():
    """
    Retrieves the list of all Class objects
    """
    all_classs = storage.all(Class).values()
    list_classs = []
    for class in all_classs:
        list_classs.append(class.to_dict())
    return jsonify(list_classs)


@app_views.route('/classs/<class_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/class/get_id_class.yml', methods=['get'])
def get_class(class_id):
    """ Retrieves a specific Class """
    class = storage.get(Class, class_id)
    if not class:
        abort(404)

    return jsonify(class.to_dict())


@app_views.route('/classs/<class_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/class/delete_class.yml', methods=['DELETE'])
def delete_class(class_id):
    """
    Deletes a Class Object
    """

    class = storage.get(Class, class_id)

    if not class:
        abort(404)

    storage.delete(class)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/classs', methods=['POST'], strict_slashes=False)
@swag_from('documentation/class/post_class.yml', methods=['POST'])
def post_class():
    """
    Creates a Class
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Class(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/classs/<class_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/class/put_class.yml', methods=['PUT'])
def put_class(class_id):
    """
    Updates a Class
    """
    class = storage.get(Class, class_id)

    if not class:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(class, key, value)
    storage.save()
    return make_response(jsonify(class.to_dict()), 200)

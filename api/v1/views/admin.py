#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Admins """
from models.admin import Admin
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/admins', methods=['GET'], strict_slashes=False)
@swag_from('documentation/admin/all_admins.yml', methods=['GET'])
def get_admins():
    """
    Retrieves the list of all admin objects
    or a specific admin
    """
    admins = storage.all(Admin).values()
    admins = [admin.to_dict() for admin in admins]
    return jsonify(admins)


@app_views.route('/admins/<admin_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/admin/get_admin.yml', methods=['GET'])
def get_admin(admin_id):
    """ Retrieves an admin """
    admin = storage.get(Admin, admin_id)
    if not admin:
        abort(404)

    return jsonify(admin.to_dict())


@app_views.route('/admins/<admin_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/admin/delete_admin.yml', methods=['DELETE'])
def delete_admin(admin_id):
    """
    Deletes a admin Object
    """
    admin = storage.get(Admin, admin_id)
    if not admin:
        abort(404)

    storage.delete(admin)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/admins', methods=['POST'], strict_slashes=False)
@swag_from('documentation/admin/post_admin.yml', methods=['POST'])
def post_admin():
    """
    Creates a admin
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")
    if 'school_name' not in request.get_json():
        abort(400, description="Missing School_name")

    data = request.get_json()
    admin = Admin(**data)
    storage.new(admin)
    storage.save()
    return make_response(jsonify(data), 201)


@app_views.route('/admins/<admin_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/admin/put_admin.yml', methods=['PUT'])
def put_admin(admin_id):
    """
    Updates a admin
    """
    admin = storage.get(Admin, admin_id)
    if not admin:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'email', 'password']:
            setattr(admin, key, value)
    storage.save()
    return make_response(jsonify(admin.to_dict()), 200)

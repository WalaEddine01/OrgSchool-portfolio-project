#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Place - Amenity """
from models.class import Place
from models.amenity import Amenity
from models import storage
from api.v1.views import app_views
from os import environ
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('schools/<school_id>/amenities', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/school_amenity/get_schools_amenities.yml',
           methods=['GET'])
def get_school_amenities(school_id):
    """
    Retrieves the list of all Amenity objects of a Place
    """
    school = storage.get(Place, school_id)

    if not school:
        abort(404)

    if environ.get('HBNB_TYPE_STORAGE') == "db":
        amenities = [amenity.to_dict() for amenity in school.amenities]
    else:
        amenities = [storage.get(Amenity, amenity_id).to_dict()
                     for amenity_id in school.amenity_ids]

    return jsonify(amenities)


@app_views.route('/schools/<school_id>/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/school_amenity/delete_school_amenities.yml',
           methods=['DELETE'])
def delete_school_amenity(school_id, amenity_id):
    """
    Deletes a Amenity object of a Place
    """
    school = storage.get(Place, school_id)

    if not school:
        abort(404)

    amenity = storage.get(Amenity, amenity_id)

    if not amenity:
        abort(404)

    if environ.get('HBNB_TYPE_STORAGE') == "db":
        if amenity not in school.amenities:
            abort(404)
        school.amenities.remove(amenity)
    else:
        if amenity_id not in school.amenity_ids:
            abort(404)
        school.amenity_ids.remove(amenity_id)

    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/schools/<school_id>/amenities/<amenity_id>', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/school_amenity/post_school_amenities.yml',
           methods=['POST'])
def post_school_amenity(school_id, amenity_id):
    """
    Link a Amenity object to a Place
    """
    school = storage.get(Place, school_id)

    if not school:
        abort(404)

    amenity = storage.get(Amenity, amenity_id)

    if not amenity:
        abort(404)

    if environ.get('HBNB_TYPE_STORAGE') == "db":
        if amenity in school.amenities:
            return make_response(jsonify(amenity.to_dict()), 200)
        else:
            school.amenities.append(amenity)
    else:
        if amenity_id in school.amenity_ids:
            return make_response(jsonify(amenity.to_dict()), 200)
        else:
            school.amenity_ids.append(amenity_id)

    storage.save()
    return make_response(jsonify(amenity.to_dict()), 201)

#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Places """
from models.class import Class
from models.student import Student
from models.class import Place
from models.admin import Admin
from models.amenity import Amenity
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/cities/<student_id>/schools', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/school/get_schools.yml', methods=['GET'])
def get_schools(student_id):
    """
    Retrieves the list of all Place objects of a Student
    """
    student = storage.get(Student, student_id)

    if not student:
        abort(404)

    schools = [school.to_dict() for school in student.schools]

    return jsonify(schools)


@app_views.route('/schools/<school_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/school/get_school.yml', methods=['GET'])
def get_school(school_id):
    """
    Retrieves a Place object
    """
    school = storage.get(Place, school_id)
    if not school:
        abort(404)

    return jsonify(school.to_dict())


@app_views.route('/schools/<school_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/school/delete_school.yml', methods=['DELETE'])
def delete_school(school_id):
    """
    Deletes a Place Object
    """

    school = storage.get(Place, school_id)

    if not school:
        abort(404)

    storage.delete(school)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/cities/<student_id>/schools', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/school/post_school.yml', methods=['POST'])
def post_school(student_id):
    """
    Creates a Place
    """
    student = storage.get(Student, student_id)

    if not student:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'admin_id' not in request.get_json():
        abort(400, description="Missing admin_id")

    data = request.get_json()
    admin = storage.get(Admin, data['admin_id'])

    if not admin:
        abort(404)

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data["student_id"] = student_id
    instance = Place(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/schools/<school_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/school/put_school.yml', methods=['PUT'])
def put_school(school_id):
    """
    Updates a Place
    """
    school = storage.get(Place, school_id)

    if not school:
        abort(404)

    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")

    ignore = ['id', 'admin_id', 'student_id', 'created_at', 'updated_at']

    for key, value in data.items():
        if key not in ignore:
            setattr(school, key, value)
    storage.save()
    return make_response(jsonify(school.to_dict()), 200)


@app_views.route('/schools_search', methods=['POST'], strict_slashes=False)
@swag_from('documentation/school/post_search.yml', methods=['POST'])
def schools_search():
    """
    Retrieves all Place objects depending of the JSON in the body
    of the request
    """

    if request.get_json() is None:
        abort(400, description="Not a JSON")

    data = request.get_json()

    if data and len(data):
        classs = data.get('classs', None)
        cities = data.get('cities', None)
        amenities = data.get('amenities', None)

    if not data or not len(data) or (
            not classs and
            not cities and
            not amenities):
        schools = storage.all(Place).values()
        list_schools = []
        for school in schools:
            list_schools.append(school.to_dict())
        return jsonify(list_schools)

    list_schools = []
    if classs:
        classs_obj = [storage.get(Class, s_id) for s_id in classs]
        for class in classs_obj:
            if class:
                for student in class.cities:
                    if student:
                        for school in student.schools:
                            list_schools.append(school)

    if cities:
        student_obj = [storage.get(Student, c_id) for c_id in cities]
        for student in student_obj:
            if student:
                for school in student.schools:
                    if school not in list_schools:
                        list_schools.append(school)

    if amenities:
        if not list_schools:
            list_schools = storage.all(Place).values()
        amenities_obj = [storage.get(Amenity, a_id) for a_id in amenities]
        list_schools = [school for school in list_schools
                       if all([am in school.amenities
                               for am in amenities_obj])]

    schools = []
    for p in list_schools:
        d = p.to_dict()
        d.pop('amenities', None)
        schools.append(d)

    return jsonify(schools)

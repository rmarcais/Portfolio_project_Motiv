#!/usr/bin/python3
"""New views for City objects"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.department import Department
from models.city import City
from models.user import User


@app_views.route('/departments/<department_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities_by_dep_id(department_id):
    """Get method to retrieve all cities based on department_id"""
    for dep in storage.all(Department).values():
        if dep.id == department_id:
            list_city = []
            for city in dep.cities:
                list_city.append(city.to_dict())
            return jsonify(list_city)
    return abort(404)


@app_views.route('/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def get_city_id(city_id):
    """Retrieves get method for a city with a given id"""
    for city in storage.all(City).values():
        if city.id == city_id:
            return jsonify(city.to_dict())
    return abort(404)


@app_views.route('/cities/<city_id>/users', methods=['GET'],
                 strict_slashes=False)
def get_city_user_id(city_id):
    """Retrieves all users of a city with a given id"""
    for city in storage.all(City).values():
        if city.id == city_id:
            u = []
            for user in city.users:
                u.append(user.to_dict())
            return jsonify(u)
    return abort(404)


@app_views.route('/departments/<department_id>/cities', methods=['POST'],
                 strict_slashes=False)
def post_city_by_dep_id(department_id):
    """ Method that create a new city based on department_id. """
    dep = storage.get(Department, department_id)
    if dep is None:
        return abort(404)

    params = request.get_json()
    if params is None:
        return abort(400, "Not a JSON")
    if "name" not in params.keys():
        return abort(400, "Missing name")
    params['department_id'] = dep.id
    new = City(**params)
    new.save()
    return jsonify(new.to_dict()), 201

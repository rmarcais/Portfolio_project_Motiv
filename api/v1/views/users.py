#!/usr/bin/python3
"""This modules defines the view for User object to handles all default API
actions"""
from flask import jsonify, abort, request, redirect
from pyrsistent import v
from models.user import User
from models.department import Department
from models.city import City
from models.sport import Sport
from models import storage
from api.v1.views import app_views, departments


@app_views.route('/users', methods=['GET'],
                 strict_slashes=False)
def get_users():
    """Retrieves get method for all users"""
    list_users = []
    all_a = storage.all(User).values()
    for user in all_a:
        list_users.append(user.to_dict())
    return jsonify(list_users)


@app_views.route('/users/<user_id>/infos', methods=['GET'],
                 strict_slashes=False)
def get_users_id(user_id):
    """Retrieves all the information of a user (base on its id)"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    city = storage.get(City, user.city_id)
    department = storage.get(Department, city.department_id)
    infos = {}
    infos['location'] = [city.name, department.name]
    infos['username'] = user.username
    infos['bio'] = user.bio
    infos['sports'] = []
    infos['events'] = []
    infos['reviews'] = []
    for s in user.sports:
        infos['sports'].append(s.name)
    for e in user.events:
        infos['events'].append(e.title)
    for r in user.reviews:
        infos['reviews'].append(r.text)
    return jsonify(infos)


@app_views.route('/users', methods=['POST'],
                 strict_slashes=False)
def post_user():
    """ Method that creates a new user. """
    params = request.get_json()
    if params is None:
        abort(400, "Not a JSON")
    if params.get("username") is None:
        abort(400, "Missing username")
    if params.get("password") is None:
        abort(400, "Missing password")
    new = User(**params)
    new.save()
    return jsonify(new.to_dict()), 201


@app_views.route('users/<user_id>',
                 methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """ Method that updates an user. """
    user = storage.get(User, user_id)
    if user is None:
        return abort(404)
    params = request.get_json()
    if params is None:
        return abort(400, "Not a JSON")
    li = ["id", "created_at", "updated_at", "username"]
    for k, v in params.items():
        if k not in li:
            setattr(user, k, v)
    user.save()
    return jsonify(user.to_dict())


@app_views.route('/users_search', methods=['POST'], strict_slashes=False)
def users_search():
    """
    Retrieves all User objects depending of the JSON in the body
    of the request
    """

    if request.get_json() is None:
        abort(400, description="Not a JSON")

    data = request.get_json()

    if data and len(data):
        departments = data.get('deps', None)
        cities = data.get('cities', None)
        sports = data.get('sports', None)
        username = data.get('username', None)

    if not data or not len(data) or (
            not cities and
            not departments and
            not sports and
            not username):
        users = storage.all(User).values()
        list_users = []
        for user in users:
            list_users.append(user.to_dict())
        return jsonify(list_users)

    list_users = []

    if departments:
        deps_obj = [storage.get(Department, d_id) for d_id in departments]
        for dep in deps_obj:
            if dep:
                for city in dep.cities:
                    if city:
                        for user in city.users:
                            list_users.append(user)

    if cities:
        city_obj = [storage.get(City, c_id) for c_id in cities]
        for city in city_obj:
            if city:
                for user in city.users:
                    if user not in list_users:
                        list_users.append(user)

    if sports:
        if not list_users:
            list_users = storage.all(User).values()
        sport_obj = [storage.get(Sport, s_id) for s_id in sports]
        list_users = [user for user in list_users
                      if all([s in user.sports
                             for s in sport_obj])]

    users = []
    if username:
        if list_users == [] and (not sports and not cities
                                 and not departments):
            list_users = storage.all(User).values()
        for u in list_users:
            if username in u.username:
                d = u.to_dict()
                d.pop("sports", None)
                users.append(d)
        return jsonify(users)

    for u in list_users:
        d = u.to_dict()
        d.pop("sports", None)
        users.append(d)

    return jsonify(users)

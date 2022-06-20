#!/usr/bin/python3
"""This modules defines the view for Department object to handles all default API
actions"""

from flask import jsonify, abort, request
from models.department import Department
from models import storage
from api.v1.views import app_views

@app_views.route('/departments', methods=['GET'],
                 strict_slashes=False)
def get_dep():
    """Retrieves get method for all departments"""
    list_dep = []
    all_dep = storage.all(Department).values()
    for dep in all_dep:
        list_dep.append(dep.to_dict())
    return jsonify(list_dep)

@app_views.route('/departments', methods=['POST'],
                 strict_slashes=False)
def post_dep():
    """ Method that create a new department. """
    params = request.get_json()
    if params is None:
        abort(400, "Not a JSON")
    if params.get("name") is None:
        abort(400, "Missing name")
    new = Department(**params)
    new.save()
    return jsonify(new.to_dict()), 201

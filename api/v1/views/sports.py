#!/usr/bin/python3
"""This modules defines the view for Sport object to handles all default API
actions"""

from flask import jsonify, abort, request
from models.sport import Sport
from models import storage
from api.v1.views import app_views


@app_views.route('/sports', methods=['GET'],
                 strict_slashes=False)
def get_sports():
    """Retrieves get method for all sports"""
    list_sports = []
    all_sports = storage.all(Sport).values()
    for sport in all_sports:
        list_sports.append(sport.to_dict())
    return jsonify(list_sports)


@app_views.route('/sports', methods=['POST'],
                 strict_slashes=False)
def post_sport():
    """ Method that create a new sport. """
    params = request.get_json()
    if params is None:
        abort(400, "Not a JSON")
    if params.get("name") is None:
        abort(400, "Missing name")
    new = Sport(**params)
    new.save()
    return jsonify(new.to_dict()), 201

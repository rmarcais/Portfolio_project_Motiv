#!/usr/bin/python3
"""This modules defines the view for User object to handles all default API
actions"""

from flask import jsonify, abort, request
from models.user import User
from models.sport import Sport
from models.review import Review
from models.event import Event
from models import storage
from api.v1.views import app_views


@app_views.route('/users/<user_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_reviews(user_id):
    """Retrieves get method for all reviews"""
    for user in storage.all(User).values():
        if user.id == user_id:
            list_r = []
            for review in user.reviews:
                list_r.append(review.to_dict())
            return jsonify(list_r)
    return abort(404)


@app_views.route('/users/<user_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def post_reviews(user_id):
    """ Method that creates a new review. """
    user = storage.get(User, user_id)
    if user is None:
        return abort(404)
    params = request.get_json()
    if params is None:
        abort(400, "Not a JSON")
    if params.get("user_id") is None:
        abort(400, "Missing user_id")
    user = storage.get(User, params['user_id'])
    if user is None:
        return abort(404)
    if params.get("text") is None:
        abort(400, "Missing text")
    params['user_id'] = user_id
    new = Review(**params)
    new.save()
    return jsonify(new.to_dict()), 201


@app_views.route('/users/<user_id>/sports', methods=['GET'],
                 strict_slashes=False)
def get_all_sports(user_id):
    """Retrieves get method for all sports of a user (based on its id)"""
    for user in storage.all(User).values():
        if user.id == user_id:
            list_s = []
            for sport in user.sports:
                list_s.append(sport.to_dict())
            return jsonify(list_s)
    return abort(404)


@app_views.route('/users/<user_id>/events', methods=['GET'],
                 strict_slashes=False)
def get_all_events(user_id):
    """Retrieves get method for all events of a user (based on its id)"""
    for user in storage.all(User).values():
        if user.id == user_id:
            list_s = []
            for event in user.events:
                list_s.append(event.to_dict())
            return jsonify(list_s)
    return abort(404)

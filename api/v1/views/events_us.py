#!/usr/bin/python3
"""This modules defines the view for Event object to handles all default API
actions"""


from flask import jsonify, abort, request
from models.user import User
from models.sport import Sport
from models.event import Event
from models import storage
from api.v1.views import app_views

@app_views.route('/events/<event_id>/sports', methods=['GET'],
                 strict_slashes=False)
def get_sport_event(event_id):
    """Retrieves get method for all sports"""
    for event in storage.all(Event).values():
        if event.id == event_id:
            sport = storage.get(Sport, event.sport_id)
            return jsonify(sport.to_dict())
    return abort(404)

@app_views.route('/events/<event_id>/users', methods=['GET'],
                 strict_slashes=False)
def get_user_event(event_id):
    """Retrieves get method for all user"""
    for event in storage.all(Event).values():
        if event.id == event_id:
            list_u = []
            for user in event.users:
                list_u.append(user.to_dict())
            return jsonify(list_u)
    return abort(404)

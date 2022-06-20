#!/usr/bin/python3
"""This modules defines the view for Event object to handles all default API
actions"""
from flask import jsonify, abort, request
from models.event import Event
from models.city import City
from models.sport import Sport
from models import storage
from api.v1.views import app_views

@app_views.route('/events', methods=['GET'],
                 strict_slashes=False)
def get_events():
    """Retrieves get method for all events"""
    list_events = []
    all_a = storage.all(Event).values()
    for e in all_a:
        list_events.append(e.to_dict())
    return jsonify(list_events)

@app_views.route('/cities/<city_id>/<sport_id>/events', methods=['POST'],
                 strict_slashes=False)
def post_event(city_id, sport_id):
    """ Method that create a new event. """
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    sport = storage.get(Sport, sport_id)
    if not sport:
        abort(404)
    params = request.get_json()
    if params is None:
        abort(400, "Not a JSON")
    if params.get("title") is None:
        abort(400, "Missing title")
    if params.get("date") is None:
        abort(400, "Missing date")
    params['city_id'] = city_id
    params['sport_id'] = sport_id
    new = Event(**params)
    new.save()
    return jsonify(new.to_dict()), 201

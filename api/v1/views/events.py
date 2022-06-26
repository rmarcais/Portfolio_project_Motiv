#!/usr/bin/python3
"""This modules defines the view for Event object to handles all default API
actions"""
from flask import jsonify, abort, request
from models.event import Event
from models.department import Department
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


@app_views.route('/events_search', methods=['POST'], strict_slashes=False)
def events_search():
    """
    Retrieves all Event objects depending of the JSON in the body
    of the request
    """

    if request.get_json() is None:
        abort(400, description="Not a JSON")

    data = request.get_json()

    if data and len(data):
        departments = data.get('deps', None)
        cities = data.get('cities', None)
        sport = data.get('sport', None)
        title = data.get('eventname', None)

    if not data or not len(data) or (
            not cities and
            not departments and
            not sport and
            not title):
        events = storage.all(Event).values()
        list_events = []
        for event in events:
            list_events.append(event.to_dict())
        return jsonify(list_events)

    list_events = []
    
    
    if departments:
        deps_obj = [storage.get(Department, d_id) for d_id in departments]
        for dep in deps_obj:
            if dep:
                for city in dep.cities:
                    if city:
                        for event in city.events:
                            list_events.append(event)

    if cities:
        city_obj = [storage.get(City, c_id) for c_id in cities]
        for city in city_obj:
            if city:
                for event in city.events:
                    if event not in list_events:
                        list_events.append(event)

    if sport:
        if not list_events:
            for e in storage.all(Event).values():
                if e.sport_id == sport[0] and len(sport) == 1:
                    list_events.append(e)
        else:
            list_all_events = []
            for e in list_events:
                if e.sport_id == sport[0] and len(sport) == 1:
                    list_all_events.append(e)

            list_events = list_all_events



    events = []
    if title:
        if list_events == [] and (not cities and not departments and not sport):
            list_events = storage.all(Event).values()
        for e in list_events:
            if title in e.title:
                d = e.to_dict()
                events.append(d)
        return jsonify(events)
    
    for e in list_events:
        d = e.to_dict()
        events.append(d)

    return jsonify(events)
#!/usr/bin/python3
"""Route to connect API"""

from api.v1.views import app_views
from flask import jsonify
from models.event import Event
from models.review import Review
from models.user import User
from models.sport import Sport
from models.city import City
from models.department import Department
import models


@app_views.route('/status', strict_slashes=False)
def status():
    """Return OK if the api is active."""
    return jsonify({'status': 'OK'})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """Returns the stats of the api"""
    motiv_class = {
        'events': models.storage.count(Event),
        'cities': models.storage.count(City),
        'departments': models.storage.count(Department),
        'reviews': models.storage.count(Review),
        'sports': models.storage.count(Sport),
        'users': models.storage.count(User)
    }
    return motiv_class

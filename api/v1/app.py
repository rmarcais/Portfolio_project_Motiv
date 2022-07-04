#!/usr/bin/python3
"""This module starts a Flask web application"""

from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception):
    """The method removes the current SQLAlchemy Session"""
    storage.close()


@app.errorhandler(404)
def page_not_found(exception):
    """ This method handle error 404 """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    cors = CORS(app, resources={'/api/v1/*': {'origins': "*"}})
    app.register_blueprint(app_views)
    host = getenv("MOTIV_HOST")
    app.run(host='0.0.0.0', port=5001, threaded=True, debug=True)

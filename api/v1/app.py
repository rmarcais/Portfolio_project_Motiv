#!/usr/bin/python3
"""This module starts a Flask web application"""

from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
cors = CORS(app, resources={'/*': {'origins': '0.0.0.0'}})
app.register_blueprint(app_views)
host = getenv("MOTIV_HOST")

@app.teardown_appcontext
def tear_down(exception):
    """The method remove the current SQLAlchemy Session"""
    storage.close()

@app.errorhandler(404)
def page_not_found(exception):
    """ This method handle error 404 """
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(host=host, port=5000, threaded=True)



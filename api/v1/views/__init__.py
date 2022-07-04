#!/usr/bin/python3
"""Initialize Blueprint"""
from flask import Blueprint

app_views = Blueprint('app_view', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.departments import *
from api.v1.views.cities import *
from api.v1.views.departments import *
from api.v1.views.sports import *
from api.v1.views.users import *
from api.v1.views.users_res import *
from api.v1.views.events import *
from api.v1.views.events_us import *

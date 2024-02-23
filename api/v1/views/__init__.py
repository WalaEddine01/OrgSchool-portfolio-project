#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.classs import *
from api.v1.views.schools import *
from api.v1.views.schools_teachers import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.admins import *
from api.v1.views.schools_amenities import *

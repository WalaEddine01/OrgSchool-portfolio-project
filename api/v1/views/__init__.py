#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.admin import *
from api.v1.views.school import *
from api.v1.views.sclass import *
from api.v1.views.student import *
from api.v1.views.teacher import *

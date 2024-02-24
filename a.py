#!/usr/bin/python3

from models import storage
from models.admin import Admin
from api.v1.views import app_views
from flask import jsonify

def get_admins():
    """
    Retrieves the list of all admin objects
    or a specific admin
    """
    admins = storage.all(Admin).values()
    admins = [admin.to_dict() for admin in admins]
    return (admins)

print(get_admins())
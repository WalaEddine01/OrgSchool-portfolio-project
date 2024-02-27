#!/usr/bin/python3
"""
initialize the models package
"""

from models import storage
from models.admin import Admin


admin = storage.get_by_key(Admin, "email", "walaa")

print(admin)


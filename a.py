#!/usr/bin/python3
"""
initialize the models package
"""

from models import storage
from models.admin import Admin
import hashlib

# User-entered password
entered_password = "wala"

# Hash the user-entered password using MD5 (or any other hashing algorithm)
hashed_entered_password = hashlib.md5("ww".encode()).hexdigest()

# Assume stored hashed password retrieved from the database
stored_hashed_password = "90a95738ba1ba41105b435092e13d1d5"  # Example hashed password

# Compare the hashed user-entered password with the stored hashed password
if hashed_entered_password == stored_hashed_password:
    print("Password is valid!")
else:
    print("Password is invalid!")



admin = storage.get_by_key(Admin, 'email', 'wala@wala.wala')






#!/usr/bin/python3
"""
This module contains the forms for the Flask app
"""
from flask_wtf import FlaskForm
import os
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from models import storage
from models.admin import Admin
from wtforms.validators import ValidationError

class regestrationForm(FlaskForm):
    """
    This class creates the registration form
    """
    school_name = StringField('School Name', validators=[DataRequired(), Length(min=2, max=24)])
    email = StringField('Email', validators=[DataRequired(), Email()])  
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    if os.environ.get('ORG_TYPE_STORAGE') != 'db':
        def validate_school_name(self, school_name):
            admin = storage.get_by_key(Admin, "school_name", school_name)
            if admin:
                raise ValidationError('That school name is taken. Please choose a different one.')

    if os.environ.get('ORG_TYPE_STORAGE') != 'db':
        def validate_email(self, email):
            admin = storage.get_by_key(Admin, "email", email)
            if admin:
                raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    """
    This class creates the login form
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

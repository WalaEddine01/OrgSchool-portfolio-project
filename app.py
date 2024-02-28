#!/usr/bin/python3

from flask import Flask, render_template, url_for, flash, redirect
from forms import *
import os
from flask_login import LoginManager, login_user, current_user
from hashlib import md5
from models import storage

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return storage.get(Admin, user_id)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('You are already logged in!', 'info')
        return redirect(url_for('home'))
    form = regestrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.school_name.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit() :
        admin = storage.get_by_key(Admin, 'email', form.email.data)
        if admin and admin.password == md5(form.password.data.encode()).hexdigest():
            login_user(admin, remember=form.remember.data)
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    # Run the app only when this script is executed directly
    app.run(debug=True, port=5002)
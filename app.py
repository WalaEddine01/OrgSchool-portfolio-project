#!/usr/bin/python3
"""
This module contains the main Flask app
"""
from flask import Flask, render_template, url_for, flash, redirect
from forms import *
import os
from flask_login import LoginManager, login_user, current_user, logout_user
from hashlib import md5
from models.admin import Admin
from models.school import School
from models.sclass import SClass
from models.student import Student
from models.teacher import Teacher
from models import storage

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    """
    This function returns the user object from the user_id
    """
    return storage.get(Admin, user_id)


@app.route('/')
@app.route('/home')
def home():
    """
    This function renders the home page
    """
    if current_user.is_authenticated:
        admin_id = current_user.id
        school = storage.get_by_key(School, 'admin_id', admin_id)
        return render_template('index.html', title='Home', name=school.name)
    return render_template('index.html', title='Home')

@app.route("/about")
def about():
    """
    This function renders the about page
    """
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    This function renders the register page
    """
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
    """
    This function renders the login page
    """
    if current_user.is_authenticated:
        flash('You are already logged in!', 'info')
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

@app.route("/logout")
def logout():
    """
    This function logs out the user
    """
    logout_user()
    return redirect(url_for('home'))

@app.route("/sclass1", methods=['GET', 'POST'])
def sclass1():
    """
    This function renders the sclass1 page
    """
    if current_user.is_authenticated:
        sclass1 = storage.get_by_key(SClass, 'name', 'SClass 1')
        sclass1_id = sclass1.id
        students = storage.all(Student)
        teachers = storage.all(Teacher)
        teachers_list = []
        students_list = []
        for student in students.values():
            if student.sclass_id == sclass1_id:
                students_list.append(student)
        for teacher in teachers.values():
            if teacher.sclass_id == sclass1_id:
                teachers_list.append(teacher)
        return render_template('sclass1.html', title='sclass1', students=students_list, teachers=teachers_list, sclass_id=sclass1_id)
    return render_template('sclass1.html', title='sclass1')

@app.route("/sclass2", methods=['GET', 'POST'])
def sclass2():
    """
    This function renders the sclass2 page
    """
    if current_user.is_authenticated:
        sclass2 = storage.get_by_key(SClass, 'name', 'SClass 2')
        sclass2_id = sclass2.id
        students = storage.all(Student)
        teachers = storage.all(Teacher)
        teachers_list = []
        students_list = []
        for student in students.values():
            if student.sclass_id == sclass2_id:
                students_list.append(student)
        for teacher in teachers.values():
            if teacher.sclass_id == sclass2_id:
                teachers_list.append(teacher)
        return render_template('sclass2.html', title='sclass2', students=students_list, teachers=teachers_list, sclass_id=sclass2_id)
    return render_template('sclass2.html', title='sclass2')

@app.route("/sclass3", methods=['GET', 'POST'])
def sclass3():
    """
    This function renders the sclass3 page
    """
    if current_user.is_authenticated:
        sclass3 = storage.get_by_key(SClass, 'name', 'SClass 3')
        sclass3_id = sclass3.id
        students = storage.all(Student)
        teachers = storage.all(Teacher)
        teachers_list = []
        students_list = []
        for student in students.values():
            if student.sclass_id == sclass3_id:
                students_list.append(student)
        for teacher in teachers.values():
            if teacher.sclass_id == sclass3_id:
                teachers_list.append(teacher)
        return render_template('sclass3.html', title='sclass3', students=students_list, teachers=teachers_list, sclass_id=sclass3_id)
    return render_template('sclass3.html', title='sclass3')

@app.route("/sclass4", methods=['GET', 'POST'])
def sclass4():
    """
    This function renders the sclass4 page
    """
    if current_user.is_authenticated:
        sclass4 = storage.get_by_key(SClass, 'name', 'SClass 4')
        sclass4_id = sclass4.id
        students = storage.all(Student)
        teachers = storage.all(Teacher)
        teachers_list = []
        students_list = []
        for student in students.values():
            if student.sclass_id == sclass4_id:
                students_list.append(student)
        for teacher in teachers.values():
            if teacher.sclass_id == sclass4_id:
                teachers_list.append(teacher)
        return render_template('sclass4.html', title='sclass4', students=students_list, teachers=teachers_list, sclass_id=sclass4_id)
    return render_template('sclass4.html', title='sclass4')

if __name__ == "__main__":
    # Run the app only when this script is executed directly
    app.run(debug=True, port=5002)
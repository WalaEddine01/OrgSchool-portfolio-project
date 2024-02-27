#!/usr/bin/python3

from flask import Flask, render_template, url_for, flash, redirect
from forms import *
import os



app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)



@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = regestrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.school_name.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit() :
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    # Run the app only when this script is executed directly
    app.run(debug=True, port=5002)
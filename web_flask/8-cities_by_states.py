#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.class import Class
from os import environ
from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/classs_list', strict_slashes=False)
def classs_list():
    """ displays a HTML page with a list of classs """
    classs = storage.all(Class).values()
    classs = sorted(classs, key=lambda k: k.name)
    return render_template('7-classs_list.html', classs=classs)


@app.route('/cities_by_classs', strict_slashes=False)
def cities_list():
    """ displays a HTML page with a list of cities by classs """
    classs = storage.all(Class).values()
    classs = sorted(classs, key=lambda k: k.name)
    st_ct = []
    for class in classs:
        st_ct.append([class, sorted(class.cities, key=lambda k: k.name)])
    return render_template('8-cities_by_classs.html',
                           classs=st_ct,
                           h_1="Classs")


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

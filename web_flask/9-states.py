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


@app.route('/classs', strict_slashes=False)
@app.route('/classs/<id>', strict_slashes=False)
def classs_class(id=""):
    """ displays a HTML page with a list of cities by classs """
    classs = storage.all(Class).values()
    classs = sorted(classs, key=lambda k: k.name)
    found = 0
    class = ""
    cities = []

    for i in classs:
        if id == i.id:
            class = i
            found = 1
            break
    if found:
        classs = sorted(class.cities, key=lambda k: k.name)
        class = class.name

    if id and not found:
        found = 2

    return render_template('9-classs.html',
                           class=class,
                           array=classs,
                           found=found)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.class import Class
from models.student import Student
from models.amenity import Amenity
from models.class import Place
from uuid import uuid4
from os import environ
from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/2-hbnb/', strict_slashes=False)
def hbnb():
    """ ORG is alive! """
    classs = storage.all(Class).values()
    classs = sorted(classs, key=lambda k: k.name)
    st_ct = []

    for class in classs:
        st_ct.append([class, sorted(class.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    schools = storage.all(Place).values()
    schools = sorted(schools, key=lambda k: k.name)

    return render_template('2-hbnb.html',
                           classs=st_ct,
                           amenities=amenities,
                           schools=schools,
                           cache_id=uuid4())


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

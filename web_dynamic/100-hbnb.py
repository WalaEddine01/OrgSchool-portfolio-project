#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.school import School
from models.student import Student
from models.sclass import SClass
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


@app.route('/100-hbnb/', strict_slashes=False)
def hbnb():
    """ ORG is alive! """
    classs = storage.all(SClass).values()
    classs = sorted(classs, key=lambda k: k.name)
    st_ct = []
    

    for c in classs:
        students = storage.all(Student).values()
        students = sorted(students, key=lambda k: k.name)
        st_ct.append([c, students])

    schools = storage.all(School).values()
    schools = sorted(schools, key=lambda k: k.name)


    return render_template('100-hbnb.html',
                           classes=st_ct,
                           schools=schools,
                           cache_id=uuid4())


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5001, debug=True, threaded=True)

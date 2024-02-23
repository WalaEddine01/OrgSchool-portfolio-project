#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.class import Class
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


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

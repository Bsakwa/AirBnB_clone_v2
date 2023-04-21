#!/usr/bin/python3

"""This module starts a Flask web application"""

from flask import Flask

app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """This function returns a string when called upon"""
    return "Hello HBNB!"

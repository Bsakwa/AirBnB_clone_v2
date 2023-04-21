#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Routes and Displays Hello HBNB!
    """
    return "Hello HBNB!"

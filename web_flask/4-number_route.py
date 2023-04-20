#!/usr/bin/python3
'''Starts a Flask web application'''

from flask import Flask

app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Displays Hello HBNB!'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hb():
    '''Displays HBNB'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''Displays C followed by the value of the variable text'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    '''Displays Python followed by a formatted text'''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''Displays a number if it is an integer'''
    if isinstance(n, int):
        return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

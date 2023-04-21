#!/usr/bin/python3

'''
Starts a Flask web application
Listens on 0.0.0.0 port 5000
Routes:
    /: Displays "Hello HBNB!"
    /hbnb: Displays "HBNB"
    /c/<text>: Displays "C" followed by the value of the variable text
'''

if __name__ == '__main__':
    from flask import Flask

    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello_hbnb():
        '''Displays Hello HBNB!'''
        return 'Hello HBNB!'

    @app.route('/hbnb')
    def hb():
        '''Displays HBNB'''
        return 'HBNB'

    @app.route('/c/<text>')
    def c(text):
        '''Displays C followed by the value of the variable text'''
        return 'C {}'.format(text.replace('_', ' '))

    app.run(host='0.0.0.0', port=5000)

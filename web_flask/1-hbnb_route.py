#!/usr/bin/python3

'''
Starts a Flask web application
listens on 0.0.0.0 port 5000
Routes:
    /: display "Hello HBNB!"
    /hbnb: display "HBNB"
'''

if __name__ == '__main__':
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

    app.run(host='0.0.0.0', port=5000)

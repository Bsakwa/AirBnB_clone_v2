#!/usr/bin/python3

'''
Starts a Flask web application
Listens on 0,0,0,0, port 5000
Routes:
    /cities_by_states: display a HTML page with a list of cities by states
'''

if __name__ == '__main__':
    from flask import Flask, render_template
    from models import storage
    app = Flask(__name__)

    @app.route('/cities_by_states', strict_slashes=False)
    def states_list():
        '''Display a HTML page with a list of Cities by States'''
        states = storage.all('State')
        return render_template('8-cities_by_states.html', states=states)

    @app.teardown_appcontext
    def teardown_db(exception):
        '''Close the current SQLAlchemy Session'''
        storage.close()

    app.run(host='0.0.0.0', port=5000)

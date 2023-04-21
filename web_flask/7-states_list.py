#!/usr/bin/python3

'''
Starts a Flask web application
Listens on 0,0,0,0, port 5000
Routes:
    /states_list: display a HTML page with a list of States
'''

if __name__ == '__main__':
    from flask import Flask, render_template
    from models import storage
    app = Flask(__name__)

    @app.route('/states_list', strict_slashes=False)
    def states_list():
        '''Display a HTML page with a list of States'''
        states = storage.all('State')
        return render_template('7-states_list.html', states=states)

    @app.teardown_appcontext
    def teardown_db(exception):
        '''Close the current SQLAlchemy Session'''
        storage.close()

    app.run(host='0.0.0.0', port=5000)

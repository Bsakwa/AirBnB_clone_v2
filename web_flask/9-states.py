#!/usr/bin/python3

'''
Starts a Flask web application
Listens on 0,0,0,0, port 5000
Routes:
    /states: display a HTML page with a list of States
    /states/<id>: display a HTML page with the State and it's Cities
'''

if __name__ == '__main__':
    from flask import Flask, render_template
    from models import storage
    app = Flask(__name__)

    @app.route('/states', strict_slashes=False)
    def states():
        '''Display a HTML page with a list of States'''
        states = storage.all('State')
        return render_template('9-states.html', states=states)

    @app.route('/states/<id>', strict_slashes=False)
    def states_id(id):
        '''Display a HTML page with the State and it's Cities'''
        states = storage.all('State')
        if id is None:
            return render_template('9-states.html')
        for state in states.values():
            if state.id == id:
                return render_template('9-states.html', state=state, id=id)
        return render_template('9-states.html')

    @app.teardown_appcontext
    def teardown_db(exception):
        '''Close the current SQLAlchemy Session'''
        storage.close()

    app.run(host='0.0.0.0', port=5000)

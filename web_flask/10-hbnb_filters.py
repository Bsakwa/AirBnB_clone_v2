#!/usr/bin/python3

''' 
Script that starts a Flask web application
Listens on 0.0.0.0 port 5000
Routes:
    /hbhb_filters: display a HTML page
'''

if __name__ =="__main__":
    from flask import Flask, render_template
    from models import storage

    app = Flask(__name__)

    @app.route('/hbnb_filters', strict_slashes=False)
    def hbnb_filters():
        ''' 
        Display a HTML page 
        '''
        states = storage.all('State')
        amenities = storage.all('Amenity')
        cities = storage.all('City')
        return render_template('10-hbnb_filters.html',
                               states=states, amenities=amenities, cities=cities)

    @app.teardown_appcontext
    def teardown_db(exception):
        '''Closes the storage on teardown'''
        storage.close()

    app.run(host='0.0.0.0', port=5000)

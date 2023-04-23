#!/usr/bin/python3

''' 
Script that starts a Flask web application
Listens on 0.0.0.0 port 5000
Routes:
    /hbhb: Display a HTML page
'''

if __name__ =="__main__":
    from flask import Flask, render_template
    from models import storage

    app = Flask(__name__)

    @app.route('/hbnb', strict_slashes=False)
    def hbnb():
        ''' 
        Display a HTML page 
        '''
        states = storage.all('State')
        amenities = storage.all('Amenity')
        places = storage.all('Place')
        return render_template('100-hbnb.html',
                               states=states, amenities=amenities, places=places)

    @app.teardown_appcontext
    def teardown_db(exception):
        '''Closes the storage on teardown'''
        storage.close()

    app.run(host='0.0.0.0', port=5000)

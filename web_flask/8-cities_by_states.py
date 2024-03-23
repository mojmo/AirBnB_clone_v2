#!/usr/bin/python3

"""
This module defines a simple Flask application with various routes
for managing and displaying states.
"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Route to display a list of all cities in States objects.

    Retrieves all State objects from the data storage,
    and renders a template to display a list of states.

    Returns:
        str: Rendered HTML template with the list of states.
    """
    states = storage.all("State")
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """Teardown function to close the data storage session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

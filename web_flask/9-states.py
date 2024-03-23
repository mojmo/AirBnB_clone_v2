#!/usr/bin/python3

"""
This module defines a simple Flask application with various routes
for managing and displaying states.
"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """
    Displays a list of all State objects sorted by name.

    Retrieves all State objects from the data storage, sorts them by name,
    and renders a template to display the list of states.

    Returns:
        str: Rendered HTML template with the list of states.
    """
    state = storage.all("State")
    return render_template('9-states.html', state=state)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    Displays a list of City objects linked to a specific State or "Not found!".

    Retrieves a specific State object by id from the data storage,
    and renders a template to display the list of cities linked to that state.
    If no State object is found with the specified id, displays "Not found!".

    Args:
        id (str): The id of the State to retrieve.

    Returns:
        str: Rendered HTML template with the list of cities or "Not found!".
    """
    for state in storage.all("State").values():
        if state.id == id:
            cities = state.cities
            return render_template("9-states.html", state=state, cities=cities)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown(exc):
    """Teardown function to close the data storage session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

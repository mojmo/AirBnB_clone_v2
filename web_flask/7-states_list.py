#!/usr/bin/python3

"""
This module defines a simple Flask application with various routes
for managing and displaying states.
"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Route to display a list of all State objects.

    Retrieves all State objects from the data storage,
    and renders a template to display a list of states.

    Returns:
        str: Rendered HTML template with the list of states.
    """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """Teardown function to close the data storage session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

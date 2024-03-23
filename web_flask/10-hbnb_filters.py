#!/usr/bin/python3

"""
Starts a Flask web application to display HBNB filters.

This module defines a Flask web application with a route
to display HBNB filters. The application retrieves and displays
all State and Amenity objects from the data storage.
"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    Route to display HBNB filters.

    Retrieves all State and Amenity objects from the data storage,
    and renders a template to display HBNB filters containing a list
    of all State and Amenity objects.

    Returns:
        str: Rendered HTML template with HBNB filters.
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")

    return render_template(
        "10-hbnb_filters.html",
        states=states,
        amenities=amenities
    )


@app.teardown_appcontext
def teardown(exc):
    """Teardown function to close the data storage session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

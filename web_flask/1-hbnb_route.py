#!/usr/bin/python3

"""A simple Flask application with various routes."""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Display a greeting message."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display 'HBNB'."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

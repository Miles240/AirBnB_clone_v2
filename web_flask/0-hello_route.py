#!/usr/bin/python3

"""Module for creating a simple Flask web page"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Route for index page"""
    return f"Hello HBNB!"


if __name__ == "__main__":
    app.run()

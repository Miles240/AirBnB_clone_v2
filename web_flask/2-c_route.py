#!/usr/bin/python3
"""Module that starts a Flask web application on port 5000"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hame():
    """Home Route"""
    return f"Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """HBNB route"""
    return f"HBNB"


@app.route("/c/<text>")
def c(text):
	"""route to c"""
	return f"C {text}"


if __name__ == "__main__":
    app.run()

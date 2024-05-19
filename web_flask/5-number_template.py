#!/usr/bin/python3
"""Module that starts a Flask web application on port 5000"""

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hame():
    """Home Route"""
    return f"Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """HBNB route"""
    return f"HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """route to c"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def text(text="is cool"):
    """route to text"""
    if text is None:
        text = request.args.get("text", "default")
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def num_template(n):
    """route to num_template"""
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run()

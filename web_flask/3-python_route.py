#!/usr/bin/python3
"""
    starts a Flask web application
    and display a string
"""
from operator import length_hint
from flask import Flask, escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    return "C %s" % escape(text.replace('_', ' '))


@app.route("/python", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def python(text):
    if text:
        return "Python %s" % escape(text.replace('_', ' '))
    return text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#!/usr/bin/python3
"""
    starts a Flask web application
    and display a string
"""
from flask import Flask
if __name__ == "__main__":
    app = Flask(__name__)

    @app.route("/", strict_slashes=False)
    def hello():
        return "Hello HBNB!"
    app.run(host="0.0.0.0", port=5000)

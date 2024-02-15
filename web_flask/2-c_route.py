#!/usr/bin/python3
"""a script that starts a Flask web application

"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Define hello function

    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Define hbnb function

    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Define text function

    """
    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

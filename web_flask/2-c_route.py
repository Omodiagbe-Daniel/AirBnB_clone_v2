#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb1():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbhb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    txt = text.replace('_', " ")
    return f"C {txt}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

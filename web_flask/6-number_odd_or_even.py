#!/usr/bin/python3
"""starts and configure Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb1():
    """return Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbhb():
    """return HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """return C + text"""
    txt = text.replace('_', " ")
    return "C " + txt


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    txt = text.replace("_", " ")
    return "Python " + txt


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", value=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
        num = "{} is even".format(n)
        return render_template("6-number_odd_or_even.html", value=num)
    elif n % 2 != 0:
        num = "{} is odd".format(n)
        return render_template("6-number_odd_or_even.html", value=num)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

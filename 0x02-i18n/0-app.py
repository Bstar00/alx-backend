#!/usr/bin/env python3
""" Flask application script """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    """ Greetings

        Return:
            Initial template html
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

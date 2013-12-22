#!/usr/bin/env python

""" Flask application that runs the YEI
    Start Something website.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

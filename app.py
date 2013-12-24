#!/usr/bin/env python

""" Flask application that runs the YEI
    Start Something website.
"""

from flask import Flask
from flask import render_template
import glob
import logging
app = Flask(__name__)


@app.route('/')
def hello():
    carousel_images = glob.glob('static/img/carousel/*.jpg')
    logging.info(carousel_images)
    return render_template(
        "index.html",
        carousel_images=carousel_images
    )


if __name__ == '__main__':
    app.run()

#!/usr/bin/env python

""" Flask application that runs the YEI
    Start Something website.
"""

from flask import Flask
from flask import render_template
import glob
import random
import models
app = Flask(__name__)


@app.route('/')
def index():
    """ Handler for the home page.
    """

    # Render the template and return it in the response.
    #
    return render_template(
        "index.html",
        instructors=models.instructors,
        workshops=models.workshops,
    )


@app.route('/carousel')
def carousel():
    """ Handler that returns our Bootstrap image carousel
        as an HTML fragment/partial.  This is loaded by
        AJAX to prevent the carousel from loading on small
        devices, when we're not showing it anyway.
    """

    # Get the list of images we want to display in
    # our carousel on the home page. Shuffle them.
    #
    carousel_images = glob.glob('static/img/carousel/*.jpg')
    random.shuffle(carousel_images)

    # Render the template and return it in the response.
    #
    return render_template(
        "partials/carousel.html",
        carousel_images=carousel_images,
    )

if __name__ == '__main__':
    app.run(debug=True)

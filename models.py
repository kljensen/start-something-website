#!/usr/bin/env python
"""
    This file contains some data in the form of Python
    objects.  We're not storing stuff in a database yet,
    but don't want to write a lot of duplicate HTML, so
    this is our solution.  These models are passed to
    templates so that the data can be rendered.
"""

kyle_bio = """
Kyle is volunteer mentor at YEI, where he helps a variety of
student and faculty&ndash;founded ventures. He is also an
angel investor, scientist, and entrepreneur.
Kyle has co-founded three ventures: Pit Rho, motorsport analytics;
PriorSmart, patent litigation analytics
(acquired by RPX Corp, Nasdaq:RPXC); and
Agrivida, renewable fuels and chemicals.
He has a Ph.D. from MIT. """

alena_bio = """
Alena is Program Director at YEI, where she leads extracurricular
programs to recruit, instruct, and support student entrepreneurs.
These programs include YEI's Tech Bootcamp, Start Something,
and the flagship Summer Fellowship. Alena is a former YEI fellow, graduate
of Yale University, and founder of a digital publishing startup.
"""

instructors = [
    {
        "name": "Alena Gribskov",
        "bio": alena_bio,
        "url": "http://www.linkedin.com/in/alenagribskov/",
        "avatar": "/static/img/alena.png",
        "links": [
            {
                "fa_icon": "fa-twitter",
                "url": "http://www.twitter.com/yeitweets"
            },
            {
                "fa_icon": "fa-linkedin",
                "url": "http://www.linkedin.com/in/alenagribskov/"
            },
        ]
    },
    {
        "name": "Kyle Jensen",
        "bio": kyle_bio,
        "url": "http://www.linkedin.com/in/kylelawrencejensen/",
        "avatar": "/static/img/kyle.png",
        "links": [
            {
                "fa_icon": "fa-github-alt",
                "url": "http://www.github.com/kljensen"
            },
            {
                "fa_icon": "fa-twitter",
                "url": "http://www.twitter.com/datakyle"
            },
            {
                "fa_icon": "fa-linkedin",
                "url": "http://www.linkedin.com/in/kylelawrencejensen/"
            },
        ]
    },
]

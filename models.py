#!/usr/bin/env python
"""
    This file contains some data in the form of Python
    objects.  We're not storing stuff in a database yet,
    but don't want to write a lot of duplicate HTML, so
    this is our solution.  These models are passed to
    templates so that the data can be rendered.
"""
import datetime

# A list of instructors, each of which is a Python dictionary.
#
instructors = [
    {
        "name": "Alena Gribskov",
        "bio": """
            Alena is Program Director at YEI, where she leads extracurricular
            programs to recruit, instruct, and support student entrepreneurs.
            These programs include YEI's Tech Bootcamp, Start Something,
            and the flagship Summer Fellowship. Alena is a former YEI fellow,
            graduate of Yale University, and founder of
            a digital publishing startup.
        """,
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
        "bio": """
            Kyle is volunteer mentor at YEI, where he helps a variety of
            student and faculty&ndash;founded ventures. He is also an
            angel investor, scientist, and entrepreneur.
            Kyle has co-founded three ventures: Pit Rho, motorsport analytics;
            PriorSmart, patent litigation analytics
            (acquired by RPX Corp, Nasdaq:RPXC); and
            Agrivida, renewable fuels and chemicals.
            He has a Ph.D. from MIT.
        """,
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

# A list of upcoming workshops. Again, each is a dictionary.
#
workshops = [
    {
        "title": "Start Something, Engineering",
        "date": datetime.date(2014, 2, 28),
        "google_docs_form_id": "1OvYqhVtJa4e1AUcoZ5hl_YYpwVOKy37vEgH5LlT6Y6k",
        "description": """
            Preference given to students in engineering and the sciences.
            Extra focus on new ventures based on primary research.
            Applications due by 1/8/2013. Location: Yale Engineering CEID.
        """,
        "show": True,
        "disabled": False,
    },
    {
        "title": "Start Something, General",
        "date": datetime.date(2014, 1, 14),
        "google_docs_form_id": "1OvYqhVtJa4e1AUcoZ5hl_YYpwVOKy37vEgH5LlT6Y6k",
        "description": """
            All students and faculty welcome. This class will help students
            prepare for the YEI summer fellowship application. Applications
            due by 2/15/2013. Location: Yale SOM.
        """,
        "show": True,
        "disabled": False,
    },
    {
        "title": "Start Something, Engineering",
        "date": datetime.date(2014, 2, 28),
        "google_docs_form_id": "1OvYqhVtJa4e1AUcoZ5hl_YYpwVOKy37vEgH5LlT6Y6k",
        "description": """
            Preference given to students in engineering and the sciences.
            Extra focus on new ventures based on primary research.
            Applications due by 1/8/2013. Location: Yale Engineering CEID.
        """,
        "show": True,
        "disabled": True,
    },
    {
        "title": "Start Something, Engineering",
        "date": datetime.date(2014, 2, 28),
        "google_docs_form_id": "1OvYqhVtJa4e1AUcoZ5hl_YYpwVOKy37vEgH5LlT6Y6k",
        "description": """
            Preference given to students in engineering and the sciences.
            Extra focus on new ventures based on primary research.
            Applications due by 1/8/2013. Location: Yale Engineering CEID.
        """,
        "show": False,
        "disabled": True,
    },
]

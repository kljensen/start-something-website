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
            programs to recruit, instruct, and support Yale entrepreneurs.
            These programs include YEI's flagship Summer Fellowship as well
            as the YEI Tech Bootcamp and Start Something programs, which she
            co&ndash;created. Alena is a former YEI fellow,
            graduate of Yale University, and founder of
            Blind Pig Media, a digital publisher.
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
            Kyle has co&ndash;founded three ventures: Pit Rho, motorsport
            analytics; PriorSmart, patent litigation analytics
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
        "title": "Start Something, General",
        "date": datetime.date(2014, 1, 14),
        "google_docs_form_id": "1zOb70KGf3R6X5vozKzX_Md3ZMQt5D452gHLbQv5hytg",
        "description": """
            All students and faculty welcome. This class will help students
            prepare for the YEI summer fellowship application. Class is FULL,
            no longer accepting new applications.
            Location:
            <a href="http://map.yale.edu/map/#building:EVANS">
            Evans Hall</a>, Yale SOM, Room 2230, Tuesday 1/14 5-10pm.
        """,
        "show": True,
        "disabled": True,
    },
    {
        "title": "Start Something, Food",
        "date": datetime.date(2014, 1, 31),
        "google_docs_form_id": "1DLGAIrjI8lbRU1xV9rWlakpNpPTE9erZDUqd9irLlY0",
        "description": """
            Preference given to students interested in food-related products
            and ventures.  Hosted in collaboration with the Yale Sustainable
            Food Project.
            Applications due by 1/26 before midnight. Location: TBD.
        """,
        "show": True,
        "disabled": False,
    },
    {
        "title": "Start Something, Engineering",
        "date": datetime.date(2014, 2, 28),
        "google_docs_form_id": "1oNuBtxXTi9IhAh7QCR6gWs5nJ4AcwKimeMRhndSypq0",
        "description": """
            Preference given to students in engineering and the
            sciences with an interest in new ventures based on primary
            research. Applications due by 2/23 before midnight.
            Location:
            <a href="http://map.yale.edu/map/#search:ceid">
            Becton Center</a>, CEID, 2/28 12-5:30pm.
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
        "show": False,
        "disabled": True,
    },
]

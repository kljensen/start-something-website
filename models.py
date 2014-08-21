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
         "name": "Margaret Lee",
        "bio": """

            Margaret Lee is Venture Creation Program (VCP) Coordinator at YEI, overseeing
            the incubation of early-stage Yale startups throughout the academic year and
            during the summer. Additionally, she supports the Yale entrepreneurial
            community and event programming. Margaret holds a B.A. from Yale University, and
            during her time at Yale, was a marketing intern with YEI, ran an international
            Model U.N. conference, and spent summers working at startups in Denver and London.
        """,
        "url": "http://www.linkedin.com/in/margaretklee",
        "avatar": "https://media.licdn.com/mpr/mpr/wc_200_200/p/1/000/1b9/1bd/08ced1e.jpg",
        "links": [
            {
                "fa_icon": "fa-twitter",
                "url": "http://www.twitter.com/yeitweets"
            },
            {
                "fa_icon": "fa-linkedin",
                "url": "http://www.linkedin.com/in/margaretklee"
            },

],
},
]

# A list of upcoming workshops. Again, each is a dictionary.
#
workshops = [
    {
        "title": "Start Something: Ideation",
        "date": datetime.date(2014, 9, 8),
        "google_docs_form_id": "1zOb70KGf3R6X5vozKzX_Md3ZMQt5D452gHLbQv5hytg",
        "description": """
            6:30-8pm. Interested in entrepreneurship but don't have a startup idea yet?
            Join us for a workshop walking you through the human-centered
            design process to generate compelling, viable business opportunities.
            Space is limited. Register by Sep. 4th by 11:59pm.
        """,
        "show": True,
        "disabled": False,
    },
    {
        "title": "Start Something: Lean Startup",
        "date": datetime.date(2014, 9, 12),
        "google_docs_form_id": "1DLGAIrjI8lbRU1xV9rWlakpNpPTE9erZDUqd9irLlY0",
        "description": """
            2-3pm. Have a startup idea and ready to take the first step? Learn the
            tactics modern entrepreneurs use to launch their ventures: the lean
            startup methodology, the basics of customer discovery, and the concept
            of product-market fit.  Space is limited. Register by Sep. 8th at 11:59pm.
        """,
        "show": True,
        "disabled": False,
    },
        {
        "title": "Start Something: Minimum Viable Products",
        "date": datetime.date(2014, 9, 15),
        "google_docs_form_id": "1DLGAIrjI8lbRU1xV9rWlakpNpPTE9erZDUqd9irLlY0",
        "description": """
            6:30-8pm. Ready to start the building your first product? Come learn what a minimum
            viable product (MVP) is, how to use it, and what the next steps are. Space
            is limited. Register by Sep. 11th at 11:59pm.
        """,
        "show": True,
        "disabled": False,
    },
        {
        "title": "Start Something: Intensive",
        "date": datetime.date(2014, 9, 19),
        "google_docs_form_id": "1oNuBtxXTi9IhAh7QCR6gWs5nJ4AcwKimeMRhndSypq0",
        "description": """
            12-5:30pm. The Start Something intensive is a special, day-long workshop
            on the fundamentals of entrepreneurship, encompassing the topics covered
            in "Ideation," "Lean Startup" and "Minimum Viable Products."  This workshop
            is for students who want a "crash course" in entrepreneurship!  Space is 
            limited and by application.  Apply by Sep. 11th at 11:59pm.
        """,
        "show": True,
        "disabled": False,
    },
        {
        "title": "Start Something: Lean Startup",
        "date": datetime.date(2014, 9, 23),
        "google_docs_form_id": "1DLGAIrjI8lbRU1xV9rWlakpNpPTE9erZDUqd9irLlY0",
        "description": """
            6:30-8pm. Have a startup idea and ready to take the first step? Learn the
            tactics modern entrepreneurs use to launch their ventures: the lean
            startup methodology, the basics of customer discovery, and the concept
            of product-market fit.  Space is limited. Register by Sep. 18th at 11:59pm.
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
            Location: Yale Engineering CEID, 2/28 12-5:30pm.
        """,
        "show": False,
        "disabled": True,
    },{
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

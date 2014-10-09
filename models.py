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
        "avatar": "http://yei.yale.edu/sites/default/files/resize/imce/MargaretLee-120x170.jpg",
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
                {
         "name": "David Cruz",
        "bio": """

            David is a co-founder of Trinity Mobile Networks and a recent Yale graduate.
            He has been involved with YEI through the Summer Fellowship in 2014 and the
            Tech Bootcamp in 2013. David is excited use his technical background to improve
            connectivity and security by creating a cost-effective mesh network through
            his own venture.
        """,
        "url": "https://www.linkedin.com/profile/view?id=343293316",
        "avatar": "http://yei.yale.edu/sites/default/files/imce/davidcruz.png",
        "links": [
            {
                "fa_icon": "fa-twitter",
                "url": "http://www.twitter.com/yeitweets"
            },
            {
                "fa_icon": "fa-linkedin",
                "url": "https://www.linkedin.com/profile/view?id=343293316"
            },
                ],
    },
                    {
         "name": "David McPeek",
        "bio": """

            David is a rising Junior at Yale, currently working as a web developer in
            digital marketing. He has been involved in YEI through the 2014 Tech Bootcamp
            and is fascinated by Lean Startup methodology for its extensibility to all
            areas of life.
        """,
        "url": "www.linkedin.com/pub/david-mcpeek/98/4b0/b59/",
        "avatar": "http://m.c.lnkd.licdn.com/mpr/pub/image-PyyhxnbTQg9OGHcVvo_7PCqcarm9IsR6OAywXUgCav2yQICMPyywX2VTapEpQsKIIgQR/david-mcpeek.jpg",
        "links": [
            {
                "fa_icon": "fa-twitter",
                "url": "http://www.twitter.com/yeitweets"
            },
            {
                "fa_icon": "fa-linkedin",
                "url": "www.linkedin.com/pub/david-mcpeek/98/4b0/b59/"
            },
                ],
    },
                {
         "name": "Ellen Su",
        "bio": """

            Ellen Su is a co-founder of 109 Design, a medical device company, where she works
            on hardware, product design, graphic design, and UI/UX. She is a former CEID Design
            Fellow, and has experience in rapid prototyping and design thinking. As an undergraduate,
            Ellen co-founded the Yale chapter of Design for America and has been a CEID Design Fellow
            and YEI Fellow since then.
        """,
        "url": "http://www.linkedin.com/pub/ellen-su/38/424/81b/",
        "avatar": "http://m.c.lnkd.licdn.com/mpr/pub/image-MdKHwBMBBGplBvejy8rBq4Kx0jw2ENsHMdrvb_0v0LnTZCO5MdKv23dB091UZNN63GA-/ellen-su.jpg",
        "links": [
            {
                "fa_icon": "fa-twitter",
                "url": "http://www.twitter.com/yeitweets"
            },
            {
                "fa_icon": "fa-linkedin",
                "url": "http://www.linkedin.com/pub/ellen-su/38/424/81b/"
            },
                ],
    },
    {
         "name": "Jacob Sandry",
        "bio": """

            Jacob is a super-Junior in Yale College majoring in American Studies.
            While he has extensive experience with non-profits both in the U.S. and
            abroad, he has most recently focused on social enterprises and mission-
            driven ventures. He was a fellow at Mosaic, a solar energy crowd-investing
            venture in Oakland, CA where he developed a platform to enable communities
            to organize solar projects. Last summer, as a Yale Entrepreneurial Institute
            summer fellow, he co-founded SOL Hydration, an innovative organic sports
            drink company. With three delicious flavors, and more on the way, he hopes
            to hydrate you soon, naturally.

        """,
        "url": "https://www.linkedin.com/profile/view?id=172984274",
        "avatar": "https://media.licdn.com/mpr/mpr/wc_200_200/p/8/000/276/048/276b63f.jpg",
        "links": [
            {
                "fa_icon": "fa-twitter",
                "url": "http://www.twitter.com/yeitweets"
            },
            {
                "fa_icon": "fa-linkedin",
                "url": "https://www.linkedin.com/profile/view?id=172984274"
            },
                ],
    },
        {
         "name": "Levi DeLuke",
        "bio": """

            Levi DeLuke is a co-founder of 109 Design, a biomedical device company that was a
            member of the 2014 YEI Summer Fellowship. He graduated from Yale in 2014 with a degree
            in Mechanical Engineering and is interested in using technology to improve healthcare.
            Levi is excited to remain in New Haven to launch the company's first product, which aims
            to improve the treatment of scoliosis.
        """,
        "url": "https://www.linkedin.com/pub/levi-deluke/54/606/b40",
        "avatar": "https://media.licdn.com/mpr/mpr/wc_200_200/p/1/005/04a/389/1b08dcb.jpg",
        "links": [
            {
                "fa_icon": "fa-twitter",
                "url": "http://www.twitter.com/yeitweets"
            },
            {
                "fa_icon": "fa-linkedin",
                "url": "https://www.linkedin.com/pub/levi-deluke/54/606/b40"
            },
                ],
    },
    
   {
         "name": "Olivia Pavco-Giaccia",
        "bio": """
            Olivia Pavco-Giaccia is junior at Yale University, majoring in cognitive science.
            Through YEI's 2013 Summer Fellowship, Olivia launched LabCandy, a social enterprise
            whose mission is to encourage young girls' interest in STEM.  Soon
            to complete a successful Kickstarter campaign, Olivia is readying to bring to market
            LabCandy's brightly colored lab coats, kid-sized sparkly lab goggles, and science
            adventure storybooks.
        """,
        "url": "",
        "avatar": "http://yei.yale.edu/sites/default/files/imce/oliviapavcogiaccia.png",
        "links": [
            {
                "fa_icon": "fa-twitter",
                "url": "http://www.twitter.com/LabCandyLLC"
            },
            {
                "fa_icon": "fa-linkedin",
                "url": "https://www.linkedin.com/pub/olivia-pavco-giaccia/"
            },
                ],
    },
    {
         "name": "Starling Childs",
        "bio": """
            Starling Childs is a recent graduate of the MEM program at the Forestry School. Prior
            to his graduate studies at Yale, Star spent several years working in the urban design
            and planning industry and holds a bachelors degree from Cornell University in Landscape
            Architecture. Star is currently working on a YEI based venture called Citiesense, which
            provides web-based economic development and planning tools for urban commercial real
            estate markets.
        """,
        "url": "http://www.linkedin.com/pub/star-childs/3/560/393/",
        "avatar": "http://m.c.lnkd.licdn.com/mpr/pub/image--HH9eDWWb4shILkBQVfkvIgQdnh-zLFPGHVPEDqmdUeccc10-HHPkGJWdmWwzzIf9U2v/star-childs.jpg",
        "links": [
            {
                "fa_icon": "fa-twitter",
                "url": "http://www.twitter.com/star_III"
            },
            {
                "fa_icon": "fa-linkedin",
                "url": "http://www.linkedin.com/pub/star-childs/3/560/393/"
            },
                ],
    },

]

# A list of upcoming workshops. Again, each is a dictionary.
#
workshops = [
        {
        "title": "Start Something: Ideation",
        "date": datetime.date(2014, 10, 13),
        "google_docs_form_id": "1WEeMGfWWcRIYU4PLWbDoGXIVFjZxpgdL1g6xDfU8NJo",
        "description": """
            6:30-8pm. Interested in entrepreneurship but don't have a startup idea yet?
           Join us for a workshop walking you through the human-centered
           design process to generate compelling, viable business opportunities.
            Space is limited. Register by Oct. 9th at 11:59pm.
        """,
        "show": True,
        "disabled": False,
    },
    {
        "title": "Start Something: Minimum Viable Products",
        "date": datetime.date(2014, 10, 15),
        "google_docs_form_id": "1VrABf7hC2EJXyoIpkRvgnJMpJeGSxgjgM0vDMZ6rqjw",
        "description": """
            6:30-8pm. Ready to start the building your first product? Come learn what a minimum
            viable product (MVP) is, how to use it, and what the next steps are. Space
            is limited. Register by Oct. 12th at 11:59pm.
        """,
        "show": True,
        "disabled": False,
    },
            {
        "title": "How to Start a Mission-Driven Venture at Yale",
        "date": datetime.date(2014, 10, 20),
        "google_docs_form_id": "1vNLJ6q678zowNHKIbY9yw7l991tW269Ous85WQ62zxI",
        "description": """
            8-9:30pm. What does it mean to start a mission-driven or "social" venture?
            Join Jacob Sandry, co-founder of SOL Hydration, for a workshop on navigating
            the social startup scene.  Learn the differences between a social and traditional
            venture, how lean startup concepts apply, and what you need to know to get
            started. Space is limited. Register by 11:59pm on Oct 16th.

        """,
        "show": True,
        "disabled": False,
    },
    {
        "title": "Make Your Startup's First Promo Video",
        "date": datetime.date(2014, 10, 27),
        "google_docs_form_id": "14IdnU1KffguKh4NiaK5WUrX7mzMrqZaZtpcRtCEV7S4",
        "description": """
            7-8:30pm. Getting ready to spread the word about your startup, or even launch
            a Kickstarter campaign?  Aily Zhang walks you through the process of making
            a useful, beautiful promotional video for your startup - no previous experience
            necessary! Space is limited. Register by October 5th at 11:59pm.
        """,
        "show": True,
        "disabled": False,
    },
    {
        "title": "Start Something @ CBEY: Intensive",
        "date": datetime.date(2014, 11, 7),
        "google_docs_form_id": "1ntWosCQ1kvRcsWo0SoEjn-bN8Y_KoRC0AmqLo-MbAWo",
        "description": """
            12-4pm. Co-hosted with the Center for Business and the Environment at Yale,
            this Start Something Intensive is a special, day-long workshop
            on the fundamentals of entrepreneurship, encompassing the topics covered
            in "Ideation," "Lean Startup" and "Minimum Viable Products."  This workshop
            is for students who want a "crash course" in entrepreneurship!  Space is
            limited and by application.  Apply by Nov. 2nd at 11:59pm.
        """,
        "show": True,
        "disabled": False,
    },
        {
        "title": "Start Something: Lean Startup",
        "date": datetime.date(2014, 10, 10),
        "google_docs_form_id": "1NnIediun4MWMBluWLTCwORO6TMYqraWrBVtNLCJ6iz8",
        "description": """
            2-3:30pm. Interested in entrepreneurship but don't have a startup idea yet?
            Join us for a workshop walking you through the human-centered
            design process to generate compelling, viable business opportunities.
            Space is limited. Register by Oct. 6th by 11:59pm.
        """,
        "show": False,
        "disabled": True,
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

YEI Start Something Website
===========================

This will be the website for YEI's "Start Something"
workshops on Lean Start-up methodology.


## Working on the site

First, check out this repo

	git clone git@github.com:yei/start-something-website.git
	cd start-something-website

Now, create a [virtualenv](https://pypi.python.org/pypi/virtualenv)
environment.

	virtualenv venv --distribute

Now, activate it

	source venv/bin/activate

Install the requirements.

	pip install -r requirements.txt

Run the app locally

	python app.py


## Deploy the application to Heroku

First, add a git remote called "heroku"

	git remote add heroku git@heroku.com:yei-start-something.git

Then, push to it

	git push heroku master

### Credits

* [Branford court photo](http://www.flickr.com/photos/pneedham/1907900037/sizes/o/)
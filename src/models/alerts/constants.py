__author__ = 'jslvtr'

import os

# changing to use Heroku Env variables
# will define these 3 environment variables inside Heroku
# when this file opens, it will load env variables into 3 below variables
# will be set in Heroku account, no one else will be able to see them in GitHub repo

URL = os.environ.get('MAILGUN_URL')
API_KEY = os.environ.get('MAILGUN_API_KEY')
FROM = os.environ.get('MAILGUN_FROM')
ALERT_TIMEOUT = 10
COLLECTION = "alerts"
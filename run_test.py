
"""
This script runs an integration test against a deployed instance of our app.
Replace HOST with the URL your project will be deployed to.
"""

import urllib2
# import logging

# The circle.yml deploys to version 1, which maps to this URL
HOST = 'https://1-dot-gae-circleci-integration.appspot.com/'

# [START e2e]
response = urllib2.urlopen("{}/".format(HOST))
html = response.read()

assert(html == "Hello world!")
# [END e2e]



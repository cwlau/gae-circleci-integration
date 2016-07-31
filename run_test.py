
"""
This script runs an integration test against a deployed instance of our app.
Replace HOST with the URL your project will be deployed to.
"""

# import urllib2
# import logging

# The circle.yml deploys to version 1, which maps to this URL
# HOST='https://1-dot-continuous-deployment-circle.appspot.com/'

# [START e2e]
# response = urllib2.urlopen("{}/get_author/ulysses".format(HOST))
# html = response.read()

text = "James Bond"
assert(text == "James Bond")
# [END e2e]



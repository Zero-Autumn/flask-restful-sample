# flask-restful-sample
A sample web app with RESTful API function built using python flask  


This app allows users to register for an API key and request the webapp for the list of books available in its database as a response .

Register for an API under /register view and note down the api key.
The registered user can send a request with their username and apikey in headers to obtain the books list in a json response.

header format:
headers={'user':username, apikey:key}

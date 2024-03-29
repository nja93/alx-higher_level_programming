#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8to the passed URL with the email
as a parameter, and displays the body of the response (decoded in utf-8
"""

import sys
from urllib import request
from urllib import parse

if __name__ == "__main__":
    # URL and email from the command line
    url = sys.argv[1]
    email = sys.argv[2]
    # Create a dict with the email parameter
    data = {'email': email}
    # Encode the data to be sent in the request body
    data_encoded = parse.urlencode(data).encode('ascii')
    # POST request to the provided URL with the email parameter created
    with request.urlopen(url, data=data_encoded) as response:
        # read and decode the response body in utf-8
        print(response.read().decode('utf-8'))

#!/usr/bin/python3
"""
Fetches a URL using the requests package and
displays information about the response body.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)
    content_type = type(response.text).__name__
    content = response.text

    print("Body response:")
    print("\t- type: {}".format(content_type))
    print("\t- content: {}".format(content))

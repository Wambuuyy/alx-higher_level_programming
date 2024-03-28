#!/usr/bin/python3
"""
Takes a URL, sends a request to the URL, and displays the body of the response.
If the HTTP status code is greater than or equal to 400, prints
"Error code:" followed by the value of the HTTP status code.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    status_code = response.status_code
    body = response.text

    if status_code >= 400:
        print("Error code:", status_code)
    else:
        print(body)

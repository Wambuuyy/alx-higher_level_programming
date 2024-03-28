#!/usr/bin/python3
"""
Fetches a URL using the requests package and
displays information about the response body.
"""

import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print(
        f'Body response:\n'
        f'\t- type: {type(response.text)}\n'
        f'\t- content: {response.text}'
          )

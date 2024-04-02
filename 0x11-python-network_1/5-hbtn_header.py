#!/usr/bin/python3
""" A script that fetches the given URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header"""

import requests
from sys import argv

if __name__ == "__main__":

    url = sys.argv[1]

    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))

#!/usr/bin/python3
""" A script that fetches the given URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header"""

import requests
import argv

if __name__ == "__main__"

    print(requests.get()argv[1]).headers.get("X-Request-Id")

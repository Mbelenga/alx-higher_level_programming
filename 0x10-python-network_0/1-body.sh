#!/bin/bash
# A script that takes in an URL and sends a GET request to it.
curl -s "$1" | wc -c

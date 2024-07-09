#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of X-request-Id
"""
import urllib.request
from sys import argv

with urllib.request.urlopen(arg[1] as res
        htmlId = res.info().get('X-Request-Id')
        print(htmlId)

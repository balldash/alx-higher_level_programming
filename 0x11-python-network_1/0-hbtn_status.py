#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
    html = res.read()
    htmlStr = html.decode('utf-8')

print('Body response:')
print("\t- type: {}".format(type(html)))
print("\t- content: {}".format(html))
print("\t- utf8 content: {}".format(htmlStr))

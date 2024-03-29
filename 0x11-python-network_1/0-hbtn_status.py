#!/usr/bin/python3
import urllib.request

# Defines the URL to fetch
# Creates a request object
# Opens the URL via with statement to close the connection
# Reads and displays the body of the response a specified format
url = "https://alx-intranet.hbtn.io/status"

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    body = response.read()

print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", body.decode('utf-8'))

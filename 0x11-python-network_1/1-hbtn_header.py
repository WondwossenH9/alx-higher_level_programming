#!/usr/bin/python3
import urllib.request
import sys
# Creates a request object and opens the URL by a with statement
# to automatically close the connection.
# Gets the x-Request-Id variable value from response header
# Checks if the script runs with URL argument and gets the URL
# from the command line argument.
def get_x_request_id(url):

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_x_request_id(url)

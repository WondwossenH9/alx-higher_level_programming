#!/usr/bin/python3
"""
Sends a POST request to the URL with the email as a parameter
and displays the body of the response decoded in utf-8.

Usage: python script_name.py <URL> <email>
"""

if __name__ == "__main__":
    import sys
    import urllib.parse
    import urllib.request

    url = sys.argv[1]
    email = sys.argv[2]

    email_data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    req = urllib.request.Request(url, data=email_data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
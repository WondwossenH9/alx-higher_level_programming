#!/usr/bin/python3
"""
Sends a request to the URL and displays body of the response in utf-8
Handles urllib.error.HTTPError exceptions and prints HTTP status code

Usage: python script_name.py <URL>
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.error

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

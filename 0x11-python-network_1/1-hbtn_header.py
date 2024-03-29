#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
that is found in the header of the response.
"""

if __name__ == "__main__":
    import sys
    import urllib.request

    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)

    with urllib.request.urlopen(sys.argv[1]) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)

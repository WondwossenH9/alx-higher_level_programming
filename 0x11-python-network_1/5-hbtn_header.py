#!/usr/bin/python3
"""
The script takes URL as input, sends a request to the URL, and display
the value of the variable X-Request-Id in the response header.
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    url = sys.argv[1]
    response = requests.get(url)
    
    request_id = response.headers.get('X-Request-Id')
    print(request_id)

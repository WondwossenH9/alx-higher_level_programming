#!/usr/bin/python3
"""
The script takes a URL as input, sends a request to the URL and displays value of 
variable X-Request-Id in the response header.
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    
    request_id = response.headers.get('X-Request-Id')
    print(request_id)

#!/usr/bin/python3
"""
The script takes URL and email address as input, sends a POST request
to the URL with the email as a parameter, and displays body of response.
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}

    response = requests.post(url, data=payload)
    
    print(response.text)

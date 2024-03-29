#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using requests package and displays body of response.
"""

if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print(f"    - type: {type(response.text)}")
    print(f"    - content: {response.text}")

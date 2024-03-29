#!/usr/bin/python3
"""
The script takes GitHub credentials (username and password) and
uses GitHub API to display your id.
"""

if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, password))
    
    if response.status_code == 200:
        user_data = response.json()
        print("Your GitHub user id is:", user_data['id'])
    else:
        print("Failed to retrieve user information. Status code:", response.status_code)

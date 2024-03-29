#!/usr/bin/python3
"""
The script fetches a URL with requests package
"""
import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    content = response.text
    print('Body response:')
    print(f'\t- type: {type(content)}')
    print(f'\t- content: {content}')

#!/usr/bin/python3
"""
The script lists 10 commits from the most recent to oldest
from a repository by a specific user using the GitHub API.
"""

if __name__ == "__main__":
    import requests
    import sys

    repository = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repository}/commits'

    response = requests.get(url)
    
    if response.status_code == 200:
        commits = response.json()[:10]  # Get the 10 most recent commits
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Failed to retrieve commits. Status code:", response.status_code)

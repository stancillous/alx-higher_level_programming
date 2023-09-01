#!/usr/bin/python3
"""script to list github commits of a repo"""

if __name__ == "__main__":
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=10"
    auth = {"Authorization": "Bearer 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"}
    r = requests.get(url)
    response = r.json()
    for item in response:
        print("{}: {}".format(item.get("sha"), item.get("commit").get("author").get("name")))

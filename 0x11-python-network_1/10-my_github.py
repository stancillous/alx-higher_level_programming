#!/usr/bin/python3
"""script to get github credentials"""

if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    auth = {"Authorization": "Bearer {}".format(password)}

    r = requests.get("https://api.github.com/user", headers=auth)
    print(r.json().get("id"))
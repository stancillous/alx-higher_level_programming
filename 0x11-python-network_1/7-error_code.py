#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)"""


if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
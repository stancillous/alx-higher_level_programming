#!/usr/bin/python3
"""script to get a specific header from a url"""

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get['X-Request-Id'])

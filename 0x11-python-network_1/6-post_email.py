#!/usr/bin/python3
"""script to send a POST request to passed url"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    emailAddress = sys.argv[2]
    data = {
        "email": emailAddress
    }
    r = requests.post(url, json=data)
    print(f"Your email is: {r.text}")

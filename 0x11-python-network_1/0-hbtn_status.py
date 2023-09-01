#!/usr/bin/python3
"""python script to fetch a url and display the body of the response"""

if __name__ == "__main__":
    import urllib.request as request

    url = "https://alx-intranet.hbtn.io/status"

    with request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))

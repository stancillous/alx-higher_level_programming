#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)"""


if __name__ == "__main__":
    from urllib.request import urlopen
    from urllib.error import HTTPError
    import sys
    url = sys.argv[1]

    try:
        with urlopen(url) as response:
            body = response.read()
            decoded_body = body.decode("utf-8")
            print(decoded_body)
    except HTTPError as err:
        print(f"Error code: {err.code}")

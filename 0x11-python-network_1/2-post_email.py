#!/usr/bin/python3
"""script to send a POST request to passed url"""

if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    import sys

    url = sys.argv[1]
    emailAddress = sys.argv[2]
    data = {
        "email": emailAddress
    }
    url_encoded_data = urlencode(data)
    utf_encoded_data = url_encoded_data.encode("utf-8")
    request_object = Request(url, utf_encoded_data)
    with urlopen(request_object) as response:
        body = response.read()
        encoded_body = body.decode("utf-8")
        print(encoded_body)

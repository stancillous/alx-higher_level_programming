#!/usr/bin/python3
# script to get a specific header from a url


if __name__ == "__main__":
    from urllib.request import urlopen
    import sys
    url = sys.argv[1]

    with urlopen(url) as response:
        body = response.read()
    print(response.getheader("X-Request-Id"))

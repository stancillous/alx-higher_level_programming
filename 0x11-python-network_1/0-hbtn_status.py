#!/usr/bin/python
# python script to fetch a url and
# display the body of the response
import urllib.request as request

url = "https://alx-intranet.hbtn.io/status"

with request.urlopen(url) as response:
    body = response.read()

print("Body response:")
print(f"\t- {body}")

    
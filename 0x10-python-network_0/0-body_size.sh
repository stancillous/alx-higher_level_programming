#!/bin/bash
# script to display size of body of a response
# after using curl
# curl -s -i $1 | grep -i 'content-length' | awk '{print $2}'
curl -s "$1" | wc -c
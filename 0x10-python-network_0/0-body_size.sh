#!/bin/bash
# script to display size of body of a response
curl -s -i $1 | grep -i 'content-length' | awk '{print $2}'
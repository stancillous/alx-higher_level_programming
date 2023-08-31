#!/bin/bash
# script to show body of response after curl
if [ $(curl -L -s -X HEAD -w "%{http_code}" "$1") == '200' ]; then curl -Ls "$1"; fi
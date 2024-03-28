#!/bin/bash
# The script takes a URL as input, sends request to URL, and displays size of the body of the response in bytes.
url=$1
curl -sI $url | grep -i Content-Length | awk '{print $2}'


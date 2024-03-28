#!/bin/bash
# This script sends a GET request to the provided URL and displays the body of a 200 status code response.
url=$1
curl -s -o response.txt -w "%{http_code}" $url | awk 'NR==1 && $0==200 {getline; print}'

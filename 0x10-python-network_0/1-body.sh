#!/bin/bash

if [ -z "$1" ]; then
    echo "Please provide a URL as an argument."
    exit 1
fi

response=$(curl -s -o temp_response.txt -w "%{http_code}" "$1")


status_code=$(tail -n1 temp_response.txt)
if [ "$status_code" -eq 200 ]; then
    echo "Response body:"
    cat temp_response.txt | sed '$d'  # Display the response body, excluding the status code
else
    echo "Response status code is $status_code. Body not displayed."
fi

rm -f temp_response.txt

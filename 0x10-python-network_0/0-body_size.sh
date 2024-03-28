#!/bin/bash

if [ -z "$1" ]; then
    echo "Please provide a URL as an argument."
    exit 1
fi

response=$(curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r')
if [ -z "$response" ]; then
    echo "Failed to get response from URL."
    exit 1
fi

echo "Size of the response body: $response bytes"

rm -f temp_response.txt

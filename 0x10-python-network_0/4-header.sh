#!/bin/bash

if [ -z "$1" ]; then
    echo "Please provide a URL as the first argument."
    exit 1
fi

response=$(curl -s -H "X-School-User-Id: 98" -o temp_response.txt "$1")

echo "Response body:"
cat temp_response.txt

rm -f temp_response.txt

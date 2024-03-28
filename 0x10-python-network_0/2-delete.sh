#!/bin/bash

if [ -z "$1" ]; then
    echo "Please provide a URL as the first argument."
    exit 1
fi

response=$(curl -s -X DELETE "$1" -o temp_response.txt)

echo "Response body:"
cat temp_response.txt

# Clean up the temporary file
rm -f temp_response.txt

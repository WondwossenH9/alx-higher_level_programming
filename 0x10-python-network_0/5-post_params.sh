#!/bin/bash

if [ -z "$1" ]; then
    echo "Please provide a URL as the first argument."
    exit 1
fi

response=$(curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -o temp_response.txt -X POST "$1")

echo "Response body:"
cat temp_response.txt

rm -f temp_response.txt

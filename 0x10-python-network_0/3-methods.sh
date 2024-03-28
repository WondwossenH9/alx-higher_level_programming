#!/bin/bash

if [ -z "$1" ]; then
    echo "Please provide a URL as the first argument."
    exit 1
fi

allowed_methods=$(curl -s -i -X OPTIONS "$1" | grep "Allow:")
echo "Allowed HTTP methods for $1:"
echo "$allowed_methods"

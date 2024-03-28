#!/bin/bash
# This script displays all HTTP methods the server will accept for the provided URL.
curl -sI -X OPTIONS $1 | grep "Allow" | cut -d " " -f 2-

#!/bin/bash
# The script makes request to 0.0.0.0:5000/catch_me to causes the server respond with a message containing You got me!
curl -s -L -X PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"

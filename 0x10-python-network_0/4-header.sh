#!/bin/bash
#Bash script that takes in a URL as an argument
curl -sX GET $1 -H "X-HolbertonSchool-User-Id: 98" -L

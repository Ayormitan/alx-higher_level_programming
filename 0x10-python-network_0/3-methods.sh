#!/bin/bash
# Script t[200~akes in a URL and displays all HTTP methods the server will accept
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-

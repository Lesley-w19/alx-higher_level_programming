#!/bin/bash
# a script that takes in a URL as an argument,sends a GET request,n displays the body
curl -s -H "X-School-User-Id: 98" "$1"

#!/bin/bash
# script that takes in a URL, sends a POST request, and displays the body of the response
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

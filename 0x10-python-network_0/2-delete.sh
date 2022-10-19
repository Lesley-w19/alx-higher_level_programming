#!/bin/bash
#  script that sends a DELETE request to the URL passed n displays the body of the response
curl -s -X DELETE "$1"

#!/bin/bash
# This Bash scripttakes in a URL, sends a request to that URL, and displays the size of the body of the response

curl -sI $URL | grep -i Content-Length

#!/bin/bash
# Script to send a request to URL and display the size of the body of the response
curl -sI $1 | grep "Content-Length" | cut -d " " -f2

#!/bin/bash
# A script that displays only the status code of the response
curl -so /dev/null --write-out "%{http_code}" "$1"

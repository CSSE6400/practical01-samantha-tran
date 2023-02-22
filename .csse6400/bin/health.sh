#!/bin/bash
#
# Check that the health endpoint is returning 200

# Start flask app
pipenv install
pipenv run flask --app todo run -p 6400 &
error=$?
pid=$!
if [[ $error -ne 0 ]]; then
    echo "Failed to start flask app"
    exit 1
fi

# Wait for flask to start
sleep 5

# Check that the health endpoint is returning 200
curl -s -o /dev/null -w "%{http_code}" http://localhost:6400/api/v1/health | grep 200
error=$?
if [[ $error -ne 0 ]]; then
    echo "Failed to get 200 from health endpoint"
    exit 1
fi

# Kill flask app
kill $pid


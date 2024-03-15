#!/bin/sh

# Run the server
echo "Running the server..."
python -m gunicorn flaskr.run:app

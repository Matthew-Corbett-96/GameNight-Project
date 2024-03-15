#!/bin/sh

# Wait for the database to be ready
echo "Waiting for the database to be ready..."
while ! nc -z $DATABASE_URL 5432; do
   sleep 0.1
done
echo "Database is ready"

# Run the server
echo "Running the server..."
python -m gunicorn flaskr.run:app

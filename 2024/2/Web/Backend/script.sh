#!/bin/sh

echo "Running preliminary setup tasks..."
echo "Waiting for database..."
while ! nc -z "$PG_HOST" "$PG_PORT"; do
  sleep 1
done
echo "Connected to database."

echo "Starting the application..."
exec npm start
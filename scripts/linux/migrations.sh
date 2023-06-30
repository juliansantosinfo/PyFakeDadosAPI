#! /bin/bash

# Migrate  database.
./manage.py makemigrations
./manage.py makemigrations api
./manage.py migrate
./manage.py collectstatic --noinput
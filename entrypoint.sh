#!/bin/sh

# only for dev purposes
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver


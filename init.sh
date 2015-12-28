#!/bin/sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username=andrew --email=a@e.ua

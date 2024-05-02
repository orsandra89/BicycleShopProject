#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (python manage.py createsuperuser --no-input)
fi
export PYTHONPATH="/opt/app/"
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic
gunicorn BicycleShopProject.wsgi --user www-data --bind 0.0.0.0:8030 --workers 1
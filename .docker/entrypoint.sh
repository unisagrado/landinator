#!/bin/bash

python manage.py collectstatic
python manage.py migrate
gunicorn landinator.wsgi -b 0.0.0.0:$PORT --log-file -
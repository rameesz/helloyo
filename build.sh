#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run database migrations (for Django projects)
python manage.py migrate

# Collect static files (for Django projects)
python manage.py collectstatic --noinput

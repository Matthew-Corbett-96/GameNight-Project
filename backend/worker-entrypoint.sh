#!/bin/sh
celery -A flaskr.run.celery worker -B --loglevel=info
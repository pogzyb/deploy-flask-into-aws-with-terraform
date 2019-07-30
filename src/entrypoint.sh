#!/usr/bin/env bash

# gunicorn --bind 0.0.0.0:${APP_PORT} run:create_app
flask run --host 0.0.0.0 --port ${APP_PORT}
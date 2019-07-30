#!/usr/bin/env bash

gunicorn --bind 0.0.0.0:${APP_PORT} run:create_app
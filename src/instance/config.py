# config.py
import os
import logging


# SECRET KEY
SECRET_KEY = os.getenv('APP_SECRET_KEY')


# Base Directory
BASEDIR = os.path.dirname(os.path.abspath(__file__))


# Logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger(__name__).setLevel(logging.INFO)


# Construct DB Connection URI
if os.getenv('FLASK_ENV') == 'production':
    SQLALCHEMY_DATABASE_URI = \
        f'postgres://' \
        f'{os.getenv("POSTGRES_USER")}:' \
        f'{os.getenv("POSTGRES_PASSWORD")}@' \
        f'{os.getenv("POSTGRES_ENDPOINT")}/' \
        f'{os.getenv("POSTGRES_DATABASE")}'
else:
    SQLALCHEMY_DATABASE_URI = \
        f'postgres://' \
        f'{os.getenv("POSTGRES_USER")}:' \
        f'{os.getenv("POSTGRES_PASSWORD")}@' \
        f'{os.getenv("POSTGRES_HOSTNAME")}:' \
        f'{os.getenv("POSTGRES_PORT")}/' \
        f'{os.getenv("POSTGRES_DATABASE")}'


# Suppress Warnings
SQLALCHEMY_TRACK_MODIFICATIONS = False

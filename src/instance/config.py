# instance/config.py
import os

SECRET_KEY = os.getenv('APP_SECRET_KEY')
BASEDIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = \
    f'postgres://' \
    f'{os.getenv("POSTGRES_USER")}:' \
    f'{os.getenv("POSTGRES_PASSWORD")}@' \
    f'{os.getenv("POSTGRES_HOSTNAME")}:' \
    f'{os.getenv("POSTGRES_PORT")}/' \
    f'{os.getenv("POSTGRES_DATABASE")}'

# config.py
import os

# postgres connection
pgs_user = os.environ.get('POSTGRES_USER')
pgs_password = os.environ.get('POSTGRES_PASSWORD')
pgs_hostname = os.environ.get('POSTGRES_HOSTNAME')
pgs_db_name = os.environ.get('POSTGRES_DB')
port = "5432"

SQLALCHEMY_DATABASE_URI = \
f"postgres://{pgs_user}:{pgs_password}@{pgs_hostname}:{port}/{pgs_db_name}"

# suppress warnings
SQLALCHEMY_TRACK_MODIFICATIONS = False

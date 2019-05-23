# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# factory
def create_app(Flask):
    app = Flask(__name__)
    # configs from configs.py
    app.config.from_object('config')
    return app

# create app
app = create_app(Flask)

# create db
db = SQLAlchemy(app)

# import views (do this last)
from . import views

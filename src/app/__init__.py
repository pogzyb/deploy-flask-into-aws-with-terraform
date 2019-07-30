# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# database object
db = None


# factory function
def create_app():
    global db
    app = Flask(__name__)
    # configs from configs.py
    app.config.from_object('config')
    # initialize database
    db = SQLAlchemy(app)
    return app


# actually create app
app = create_app()

# import views
from . import views

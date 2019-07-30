# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# database object
db = None


# app factory function
def create_app():
    global db
    app = Flask(__name__, instance_relative_config=True)
    with app.app_context():
        # configs from configs.py
        app.config.from_pyfile('config.py')
        # initialize database
        db = SQLAlchemy(app)

    return app


app = create_app()


from . import views

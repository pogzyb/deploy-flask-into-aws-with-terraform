# app/__init__.py
from flask import Flask


# app factory function
def create_app():
    global db
    # initialize flask instance
    app = Flask(__name__, instance_relative_config=True)
    # configs from configs.py
    app.config.from_pyfile('config.py')
    with app.app_context():
        # register views
        from . import views
        app.register_blueprint(views.homepage)
        app.register_blueprint(views.api)
        # initialize database
        from .models import db
        db.init_app(app)
        db.create_all()
    return app


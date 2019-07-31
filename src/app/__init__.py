# app/__init__.py
from flask import Flask


db = None
tm = None


# app factory function
def create_app():
    global db
    global tm
    # initialize flask instance
    app = Flask(__name__, instance_relative_config=True)
    # configs from configs.py
    app.config.from_pyfile('config.py')
    with app.app_context():
        # initialize database
        from .models import db
        db.init_app(app)
        db.create_all()
        # initialize task manager
        from .tasks import TaskManager
        tm = TaskManager()
        tm.init_app(app, db)
        # register views
        from .views import webpage, api
        app.register_blueprint(webpage)
        app.register_blueprint(api)

    return app


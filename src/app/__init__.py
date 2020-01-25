# app/__init__.py
from flask import Flask
import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger(__name__).setLevel(logging.INFO)


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    from app.models import db
    db.init_app(app)
    from app.tasks import tm
    tm.init_app(app, db)
    with app.app_context():
        db.create_all()
        from app.blueprints import web, api
        app.register_blueprint(web)
        app.register_blueprint(api, url_prefix='/api')
    return app


# src/app/models.py
from flask_sqlalchemy import SQLAlchemy
import datetime


db = SQLAlchemy()

"""
Models: the database objects
"""


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    birthday = db.Column(
        db.TIMESTAMP,
        server_default=db.func.current_timestamp(),
        nullable=False
    )

    def __init__(self, uid, name, birthday=None):
        self.uid = uid
        self.name = name
        if isinstance(birthday, datetime.datetime):
            self.birthday = birthday

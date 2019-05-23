# app/models.py
from app import app, db

## database models

class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    birthday = db.Column(db.TIMESTAMP,
        server_default=db.func.current_timestamp(),
        nullable=False
    )

    def __init__(self, uid, name):
        self.uid = uid
        self.name = name

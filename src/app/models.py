# app/models.py
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY
from flask_sqlalchemy import SQLAlchemy
from enum import Enum


db = SQLAlchemy()


class Status(Enum):
    pending = 'Pending'
    complete = 'Complete'
    failed = 'Failed'


class Wiki(db.Model):
    __tablename__ = 'wiki'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(64), nullable=False)
    term = db.Column(db.String(250), unique=True, nullable=False)
    status = db.Column(sa.Enum(Status), nullable=False, info={'enum_class': Status})
    messages = db.Column(ARRAY(sa.String(250)))
    links = db.Column(ARRAY(sa.String(250)))

# src/app/views.py
from .models import db, Person
from flask import Blueprint, jsonify, request, render_template
from uuid import uuid1
import logging


"""
Blueprint Views
"""

# simple homepage
homepage = Blueprint('home', __name__, template_folder='templates')


@homepage.route('/', methods=['GET', 'POST'])
def home():
    """
    This is the homepage of the app, and displays every Person in the database

    :return: renders the index.html template with database data
    """
    people = Person.query.all()
    if request.method == 'GET':
        return render_template('home.html', items={'people': people, 'alert': None})
    elif request.form:
        data = request.form
        exists = Person.query.filter_by(name=data['name']).first()
        if exists:
            payload = {'people': people, 'alert': ('danger', f'{data["name"]} already exists!')}
            return render_template('home.html', items=payload)
        # doesn't exist; generate new Person
        uid = str(uuid1())
        p = Person(uid=uid, name=data['name'])
        db.session.add(p)
        db.session.commit()
        people = Person.query.all()
        payload = {'people': people, 'alert': ('success', f'{data["name"]} was added!')}
        return render_template('home.html', items=payload)


# api routes
api = Blueprint('api', __name__)


@api.route('/new', methods=['POST'])
def new():
    """
    This is an API method to add something new to the database

    :return: json payload w/ uid of new Person if successful
    """
    data = request.get_json()
    exists = Person.query.filter_by(name=data['name']).first()
    if exists:
        return jsonify({'status': 'This already exists!'}), 409
    # doesn't exist; generate new Person
    uid = str(uuid1())
    p = Person(uid=uid, name=data['name'])
    db.session.add(p)
    db.session.commit()
    return jsonify({'status': 'success', 'uid': uid}), 201


@api.route('/one/<uid>', methods=['GET'])
def one(uid):
    """
    This is an API method to retrieve one record from the database

    :param uid: a unique id to look up in the database
    :return: json payload - single Person if found
    """
    person = Person.query.filter_by(uid=uid).first()
    if not person:
        return jsonify({'status': 'not found'}), 404
    payload = {
        'name': person.name,
        'uid': person.uid,
        'birthday': str(person.birthday),
    }
    return jsonify({'status': 'success', 'data': payload}), 200


@api.route('/all', methods=['GET'])
def everything():
    """

    :return: json payload - everything in the Person model
    """
    peeps = Person.query.all()
    return jsonify({'status': 'success', 'data': peeps}), 200


"""
Threading: Long-running background task
"""
@api.route('/long-task', methods=['POST'])
def background():
    try:
        pass
    except Exception as e:
        logging.debug(f'{e}')
        return
    return


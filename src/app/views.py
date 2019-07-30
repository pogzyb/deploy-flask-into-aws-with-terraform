# app/views.py
from . import app, db
from .models import Person
from flask import jsonify, request, render_template
from uuid import uuid1
import threading


"""
Define Routes and Populate Views
"""
@app.route('/', methods=['GET'])
def home():
    """
    This is the homepage of the app, and displays every Person in the database

    :return: renders the home.html template with database data
    """
    people = Person.query.all()
    return render_template('home.html', items=people)


@app.route('/new', methods=['POST'])
def new():
    """
    This is a both a Form and API method to add something new to the database

    :return: json payload w/ uid of new Person if successful
    """
    if request.form:
        data = request.form
    else:
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


@app.route('/one/<uid>', methods=['GET'])
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


@app.route('/all', methods=['GET'])
def everything():
    """

    :return: json payload - everything in the Person model
    """
    peeps = Person.query.all()
    return jsonify({'status': 'success', 'data': peeps}), 200


"""
Threading example: Long-running background task
"""
@app.route('/long-task', methods=['POST'])
def background():
    return

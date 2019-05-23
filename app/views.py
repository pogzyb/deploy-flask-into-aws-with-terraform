# app/views.py
from flask import jsonify, request, render_template
from app import app, db
from app.models import Person
from uuid import uuid1
import os


## app routes and views
@app.route('/')
def home(methods=['GET']):
    peeps = Person.query.all()
    return render_template('home.html', items=peeps)


# add one to db
@app.route('/new', methods=['POST'])
def new():
    if request.form:
        data = request.form
    else:
        data = request.get_json()
    print(data)
    # exists already
    exists = Person.query.filter_by(name=data['name']).first()
    if exists:
        return jsonify({'status': 'already exists!'}), 409
    # generate uid
    uid = str(uuid1())
    # create new person
    p = Person(uid=uid, name=data['name'])
    # add to db
    db.session.add(p)
    db.session.commit()
    # return success
    return jsonify({'status': 'success', 'uid': uid}), 201


# return one
@app.route('/one/<uid>', methods=['GET'])
def one(uid):
    p = Person.query.filter_by(uid=uid).first()
    payload = {
        'name': p.name,
        'uid': p.uid,
        'birthday': str(p.birthday),
    }
    if p:
        return jsonify({'status': 'success', 'data': payload}), 201
    else:
        return jsonify({'status': 'not found'}), 404


# return it all
@app.route('/all', methods=['GET'])
def all():
    peeps = Person.query.all()
    return jsonify({'status': 'success', 'data': peeps}), 200


# create database models
db.create_all()

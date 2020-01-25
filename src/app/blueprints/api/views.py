# app/blueprints/api/views.py
from flask import (
    Blueprint,
    jsonify,
    request
)
from uuid import uuid1
import logging

from app.models import Wiki
from app.tasks import tm


logger = logging.getLogger(__name__)

# define "api" blueprint
api = Blueprint('api', __name__)


@api.route('/new', methods=['POST'])
def new():
    data = dict(request.json)
    data['uid'] = str(uuid1())
    term = data.get('term')
    tm.create_task(data=data)
    payload = {
        'term': term,
        'info': f'check the status for this term @ "/api/one/{term}"'
    }
    return jsonify({'status': 'success', 'data': payload}), 201


@api.route('/one/<string:term>', methods=['GET'])
def one(term):
    wiki = Wiki.query.filter_by(term=term).first()
    if not wiki:
        return jsonify({'status': 'not found'}), 404
    payload = {
        'term': wiki.term,
        'status': wiki.status.value,
        'messages': wiki.messages,
        'links': wiki.links,
    }
    return jsonify({'status': 'success', 'data': payload}), 200


@api.route('/all', methods=['GET'])
def everything():
    payload = []
    all_wikis = Wiki.query.all()
    for wiki in all_wikis:
        individual = {
            'term': wiki.term,
            'status': wiki.status.value,
            'messages': wiki.messages,
            'links': wiki.links,
        }
        payload.append(individual)
    return jsonify({'status': 'success', 'data': payload}), 200


@api.route('/poll/<string:term>', methods=['GET'])
def poll(term: str):
    wiki = tm.get_record(term)
    payload = {
        'messages': wiki.messages,
        'status': wiki.status.value
    }
    return jsonify({'status': 'success', 'poll': payload}), 200

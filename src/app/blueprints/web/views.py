# app/blueprints/web/views.py
from flask import (
    Blueprint,
    request,
    render_template,
    url_for,
    redirect
)
from uuid import uuid1
import logging

from app.tasks import tm
from app.models import Wiki


logger = logging.getLogger(__name__)

# define "web" blueprint
web = Blueprint('web', __name__, template_folder='templates')


@web.route('/', methods=['GET', 'POST'])
def home():
    """
    This is the homepage of the app.
    Right now, it displays every "Wiki" search done in the database
    """
    wikis = Wiki.query.all()
    return render_template('home.html', items={'wikis': wikis, 'alert': None})


@web.route('/background', methods=['POST'])
def background():
    try:
        form = dict(request.form)
        form['uid'] = str(uuid1())
        exists = Wiki.query.filter_by(term=form['term']).first()
        if exists:
            return redirect(url_for('.home'))
        else:
            tm.create_task(data=form)
        return redirect(url_for('.status', term=form.get('term')))
    except Exception as e:
        people = Wiki.query.all()
        return render_template('home.html', items={'people': people, 'alert': ('danger', f'{e}')})


@web.route('/status/<term>', methods=['GET'])
def status(term: str):
    record = tm.get_record(term)
    if not record:
        wikis = Wiki.query.all()
        return render_template('home.html', items={
            'wikis': wikis,
            'alert': ('danger', f'Could not find a task for {term}')
        })
    else:
        return render_template('status.html', items={'wiki': record})

# app/tasks.py
from concurrent.futures import ThreadPoolExecutor, Future
from threading import RLock
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from typing import Dict, Any
import random
import logging
import datetime
import time

from app.models import Wiki, Status


logger = logging.getLogger(__name__)


class TaskManager(object):
    """
    Manages kicking off "Tasks" and returning tracking their results
    """
    def __init__(self, max_workers: int = 2):
        self.task_status_map = {}
        self._pool = ThreadPoolExecutor(max_workers=max_workers)
        self._lock = RLock()
        self._app = None
        self._db = None

    def init_app(self, app: Flask, db: SQLAlchemy) -> None:
        self._app = app
        self._db = db

    def create_task(self, data) -> None:
        term = data.get('term')
        task = Task(
            uid=data.get('uid'),
            app_ref=self._app,
            db_ref=self._db,
            tm_ref=self
        )
        submitted_task = self._pool.submit(task.do_search, data, self._lock)
        logger.info(f'Submitted task for {term}')
        submitted_task.add_done_callback(task.done_callback)

    def get_record(self, term: str) -> Wiki:
        with self._app.app_context():
            record = self._db.session.query(Wiki).filter_by(term=term).first()
            if not record:
                return None
            else:
                return record

    def check_done(self, term: str) -> bool:
        with self._app.app_context():
            record = self._db.session.query(Wiki).filter_by(term=term).first()
            if not record:
                return False
            return record.status == Status.complete

    def update_status(self, uid: str, status: Status) -> None:
        with self._app.app_context():
            record = self._db.session.query(Wiki).filter_by(uid=uid).first()
            record.status = status
            self._db.session.commit()
            logger.info(f'Updated status for {record.term}')

    def update_messages(self, term: str, message: str) -> None:
        with self._app.app_context():
            record = self._db.session.query(Wiki).filter_by(term=term).first()
            modified = list(record.messages)
            modified.append(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {message}')
            record.messages = modified
            self._db.session.commit()
        logger.info(f'Updated messages for {term}')


class Task(object):
    """
    Performs the actual Task and saves results to the database
    """
    def __init__(self, uid: str, app_ref: Flask, db_ref: SQLAlchemy, tm_ref: TaskManager):
        self._app = app_ref
        self._db = db_ref
        self._tm = tm_ref
        self._uid = uid
        self._status = Status.pending

    def do_search(self, data: Dict[str, Any], lock: RLock) -> None:
        with lock:
            term = data.get('term')
            logger.info(f'Acquired Locked! Saving initial data for {term}')
            search = Wiki(
                term=term,
                uid=self._uid,
                status=self._status,
                messages=[
                    f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - Starting Wikipedia scrape for {term}!'
                ]
            )
            with self._app.app_context():
                self._db.session.add(search)
                self._db.session.commit()
            logger.info(f'Releasing Lock! Saved {term}')

        # search and parse Wikipedia
        time.sleep(random.randint(0, 10))
        self._tm.update_messages(term, 'Almost done!')
        time.sleep(random.randint(0, 10))
        self._status = Status.complete

    def done_callback(self, fut_obj: Future) -> None:
        fut_obj.result()
        logger.info(f'Attempting to update status to {self._status.value}')
        self._tm.update_status(self._uid, self._status)


tm = TaskManager()

# src/app/tasks.py
from .models import Person
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from time import sleep
from uuid import uuid1
import threading
import logging
import copy


logger = logging.getLogger(__name__)

"""
TaskManager handles spawning long-running
background tasks in separate threads.
"""


class TaskStatus(object):
    """
    Status updates displayed to the user.
    """

    def __init__(self):
        self.status = f'{str(datetime.now())} -- Starting!'
        self.messages = [self.status]

    def update_status(self, new_status: str) -> None:
        self.status = new_status
        self.messages.append(new_status)


class TaskManager(object):
    """
    Handles spawning new threads
    """

    def __init__(self):
        self.task_map = dict()
        self.task_status_map = dict()
        self._lock = threading.RLock()

    def init_app(self, app: Flask, db: SQLAlchemy):
        self.app = app
        self.db = db

    def create_task(self, item: str):
        with self._lock:
            if self.get_status(item):
                return  # already doing it
            task = Task(self, self.app, self.db)
            self.task_map[item] = task
            # task manager gets its own task status object to work with
            self.task_status_map[item] = TaskStatus()
            task.entrypoint(item)
            return

    def get_status(self, item: str) -> TaskStatus:
        with self._lock:
            return self.task_status_map.get(item)

    def update_task_status_object(self, task_status_obj: TaskStatus, item: str):
        with self._lock:
            self.task_status_map[item] = task_status_obj

    def destroy_task(self):
        """
        Remove tasks that are done. WIP

        :return:
        """
        pass


class Task(object):
    """
    Does the background task in its own thread
    """

    def __init__(self, tm_reference: TaskManager, app_reference: Flask, db_reference: SQLAlchemy):
        self.tm = tm_reference
        self.app = app_reference
        self.db = db_reference
        self.ts = TaskStatus()

    def update_task_status(self, new_status, item: str):
        status_string = f'{str(datetime.now())} -- {new_status}'
        self.ts.update_status(status_string)
        self.push_new_status_to_manager(item)

    def push_new_status_to_manager(self, item: str):
        self.tm.update_task_status_object(copy.deepcopy(self.ts), item)

    def entrypoint(self, item: str):
        """
        Mimics long task by taking 15 seconds to insert a record

        :param item:
        :return:
        """
        thread = threading.Thread(target=self.run_task, args=(item,), daemon=True)
        thread.start()

    def run_task(self, item: str):
        with self.app.app_context():
            logger.info(f'Working on {item}!')
            self.update_task_status('Running fast!', item)
            sleep(5)
            self.update_task_status('Still running!', item)
            person = Person(name=item, uid=str(uuid1()))
            exists = self.db.session.query(Person).filter_by(name=item).first()
            if exists:
                self.update_task_status(f'{item} already exists!', item)
                self.update_task_status(f'...so I\'m Done!', item)
                return
            sleep(5)
            self.update_task_status('Stopping!', item)
            self.db.session.add(person)
            self.db.session.commit()
            sleep(5)
            self.update_task_status(f'{item} was added to the Database!', item)
            self.update_task_status('I\'m Done!', item)
            self.tm.destroy_task()


# single instance
tm = TaskManager()

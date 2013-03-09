# -*- coding: utf-8 -*-

from datetime import datetime


class Task(object):
    def __init__(self, title):
        super(Task, self).__init__()
        self.title = title
        self.visible = True
        self.done = False


class Tasklist(object):
    def __init__(self):
        super(Tasklist, self).__init__()
        self.tasks = []

    def add(self, title):
        new_task = Task(title)
        self.tasks.insert(0, new_task)

    def complete(self, task_nr):
        self.tasks[task_nr].done = True

    def hide_finished(self):
        for task in self.tasks:
            if task.done:
                task.visible = False

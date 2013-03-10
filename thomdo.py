# -*- coding: utf-8 -*-
"""
Thomdo

A simple todo-list application written in Python + PySide
"""

import sys
import json
from PySide import QtCore, QtGui
from thomdo_gui import Ui_Thomdo


class Thomdo(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Thomdo, self).__init__(parent)
        self.ui = Ui_Thomdo()
        self.ui.setupUi(self)

        self.ui.entryField.returnPressed.connect(self.return_pressed)
        self.ui.clearButton.clicked.connect(self.clear)
        self.ui.saveButton.clicked.connect(self.save)
        self.ui.loadButton.clicked.connect(self.load)

    def clear(self):
        for item in self._tasks():
            if item.checkState() == QtCore.Qt.Checked:
                row = self.ui.taskList.row(item)
                self.ui.taskList.takeItem(row)

    def save(self):
        with open("tasks.json", "w") as f:
            json.dump(self._tasks_dict(), f)

    def load(self):
        with open("tasks.json", 'rb') as f:
            tasks = json.loads(f.read())
            self.ui.taskList.clear()
            for task in tasks:
                self._add_task(task['title'], task['done'])

    def return_pressed(self):
        entered_text = self.ui.entryField.text()
        if entered_text != "":
            self.ui.entryField.clear()
            self._add_task(entered_text, False)

    def _tasks(self):
        tasklist = self.ui.taskList
        return [tasklist.item(i) for i in range(tasklist.count())]

    def _tasks_dict(self):
        json_tasks = []
        for task in self._tasks():
            done = (task.checkState() == QtCore.Qt.Checked)
            json_task = {"title": task.text(), "done": done}
            json_tasks.insert(0, json_task)
        return json_tasks

    def _add_task(self, title, checked):
        item = QtGui.QListWidgetItem()
        item.setText(title)
        if checked:
            item.setCheckState(QtCore.Qt.Checked)
        else:
            item.setCheckState(QtCore.Qt.Unchecked)
        self.ui.taskList.insertItem(0, item)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    thomdo = Thomdo()
    thomdo.show()
    sys.exit(app.exec_())

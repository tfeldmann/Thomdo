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
        """ clears checked items """
        for item in self._tasks():
            if item.checkState() == QtCore.Qt.Checked:
                row = self.ui.taskList.row(item)
                self.ui.taskList.takeItem(row)

    def save(self):
        """ saves the task as a json file """
        with open("tasks.json", "w") as f:
            json.dump(self._tasks_dict(), f)

    def load(self):
        """ parses a saved json task file and fills the list """
        with open("tasks.json", 'rb') as f:
            tasks = json.loads(f.read())
            self.ui.taskList.clear()
            for task in tasks:
                self._add_task(task['title'], task['done'])

    def return_pressed(self):
        """ clears the line edit and inserts the task """
        entered_text = self.ui.entryField.text()
        if entered_text != "":
            self.ui.entryField.clear()
            self._add_task(entered_text, False)

    def _tasks(self):
        """ returns all tasks as a list of QListWidgetItems """
        tasklist = self.ui.taskList
        return [tasklist.item(i) for i in range(tasklist.count())]

    def _tasks_dict(self):
        """ returns all tasks as array of dictionaries """
        dicts = []
        for task in self._tasks():
            done = (task.checkState() == QtCore.Qt.Checked)
            dict = {"title": task.text(), "done": done}
            dicts.insert(0, dict)
        return dicts

    def _add_task(self, title, checked):
        """ inserts a task at the beginning of the ui.taskList widget """
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
    app.exec_()

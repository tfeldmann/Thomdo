# -*- coding: utf-8 -*-

import sys
import json
from PySide import QtCore, QtGui
from thomdo_gui import Ui_Thomdo
from tasklist import Tasklist


class Thomdo(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Thomdo, self).__init__(parent)
        self.ui = Ui_Thomdo()
        self.ui.setupUi(self)
        self.ui.entryField.returnPressed.connect(self.return_pressed)
        self.ui.clearButton.clicked.connect(self.clear)
        self.task_model = Tasklist()

    def clear(self):
        self.task_model.hide_finished()
        self.update_list_entries()

    def return_pressed(self):
        entered_text = self.ui.entryField.text()
        if entered_text != "":
            self.ui.entryField.clear()
            self.task_model.add(entered_text)
            self.update_list_entries()

    def update_list_entries(self):
        self.ui.taskList.clear()
        for task in self.task_model.tasks:
            if task.visible:
                item = QtGui.QListWidgetItem()
                item.setText(task.title)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.ui.taskList.addItem(item)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    thomdo = Thomdo()
    thomdo.show()
    sys.exit(app.exec_())

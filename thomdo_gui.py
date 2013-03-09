# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thomdo_gui.ui'
#
# Created: Fri Mar  8 23:18:11 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Thomdo(object):
    def setupUi(self, Thomdo):
        Thomdo.setObjectName("Thomdo")
        Thomdo.resize(414, 407)
        Thomdo.setMinimumSize(QtCore.QSize(0, 0))
        Thomdo.setSizeGripEnabled(True)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Thomdo)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.entryField = QtGui.QLineEdit(Thomdo)
        self.entryField.setObjectName("entryField")
        self.verticalLayout.addWidget(self.entryField)
        self.taskList = QtGui.QListWidget(Thomdo)
        self.taskList.setFocusPolicy(QtCore.Qt.NoFocus)
        self.taskList.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.taskList.setObjectName("taskList")
        self.verticalLayout.addWidget(self.taskList)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.clearButton = QtGui.QPushButton(Thomdo)
        self.clearButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clearButton.setObjectName("clearButton")
        self.verticalLayout_2.addWidget(self.clearButton)
        self.saveButton = QtGui.QPushButton(Thomdo)
        self.saveButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout_2.addWidget(self.saveButton)
        self.loadButton = QtGui.QPushButton(Thomdo)
        self.loadButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.loadButton.setObjectName("loadButton")
        self.verticalLayout_2.addWidget(self.loadButton)
        self.versionLabel = QtGui.QLabel(Thomdo)
        self.versionLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.versionLabel.setObjectName("versionLabel")
        self.verticalLayout_2.addWidget(self.versionLabel)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Thomdo)
        QtCore.QMetaObject.connectSlotsByName(Thomdo)
        Thomdo.setTabOrder(self.entryField, self.taskList)
        Thomdo.setTabOrder(self.taskList, self.clearButton)
        Thomdo.setTabOrder(self.clearButton, self.saveButton)
        Thomdo.setTabOrder(self.saveButton, self.loadButton)

    def retranslateUi(self, Thomdo):
        Thomdo.setWindowTitle(QtGui.QApplication.translate("Thomdo", "ThomDo", None, QtGui.QApplication.UnicodeUTF8))
        self.entryField.setPlaceholderText(QtGui.QApplication.translate("Thomdo", "Neuer Eintrag", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("Thomdo", "Aufräumen", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("Thomdo", "Speichern", None, QtGui.QApplication.UnicodeUTF8))
        self.loadButton.setText(QtGui.QApplication.translate("Thomdo", "Laden", None, QtGui.QApplication.UnicodeUTF8))
        self.versionLabel.setText(QtGui.QApplication.translate("Thomdo", "ThomDo 1.0", None, QtGui.QApplication.UnicodeUTF8))


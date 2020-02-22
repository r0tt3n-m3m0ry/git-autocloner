# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(560, 758)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 541, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.links = QtWidgets.QPlainTextEdit(Form)
        self.links.setGeometry(QtCore.QRect(10, 120, 541, 521))
        self.links.setObjectName("links")
        self.btn_clone = QtWidgets.QPushButton(Form)
        self.btn_clone.setGeometry(QtCore.QRect(10, 650, 541, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_clone.setFont(font)
        self.btn_clone.setObjectName("btn_clone")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Git Autocloner"))
        self.label.setText(_translate("Form", "Git Autocloner by Oleg Voevodin"))
        self.links.setPlaceholderText(_translate("Form", "Please, enter GitHub repositories links, one link by one string\n\nALL LINKS MUST CONTAIN PROTOCOL TOO!"))
        self.btn_clone.setText(_translate("Form", "Clone!"))

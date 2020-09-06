# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GitAutocloner(object):
    def setupUi(self, GitAutocloner):
        GitAutocloner.setObjectName("GitAutocloner")
        GitAutocloner.resize(560, 758)
        self.header = QtWidgets.QLabel(GitAutocloner)
        self.header.setGeometry(QtCore.QRect(10, 10, 541, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.header.setFont(font)
        self.header.setFrameShape(QtWidgets.QFrame.Box)
        self.header.setLineWidth(2)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.links = QtWidgets.QPlainTextEdit(GitAutocloner)
        self.links.setGeometry(QtCore.QRect(10, 170, 541, 471))
        self.links.setObjectName("links")
        self.btn_clone = QtWidgets.QPushButton(GitAutocloner)
        self.btn_clone.setGeometry(QtCore.QRect(10, 650, 541, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_clone.setFont(font)
        self.btn_clone.setObjectName("btn_clone")
        self.profile = QtWidgets.QLineEdit(GitAutocloner)
        self.profile.setGeometry(QtCore.QRect(140, 130, 301, 31))
        self.profile.setObjectName("profile")
        self.btn_clone_all = QtWidgets.QPushButton(GitAutocloner)
        self.btn_clone_all.setGeometry(QtCore.QRect(450, 130, 101, 31))
        self.btn_clone_all.setObjectName("btn_clone_all")
        self.is_clone_all = QtWidgets.QCheckBox(GitAutocloner)
        self.is_clone_all.setGeometry(QtCore.QRect(10, 130, 121, 31))
        self.is_clone_all.setObjectName("is_clone_all")

        self.retranslateUi(GitAutocloner)
        QtCore.QMetaObject.connectSlotsByName(GitAutocloner)

    def retranslateUi(self, GitAutocloner):
        _translate = QtCore.QCoreApplication.translate
        GitAutocloner.setWindowTitle(_translate("GitAutocloner", "Git Autocloner"))
        self.header.setText(_translate("GitAutocloner", "Git Autocloner by Oleg Voevodin"))
        self.links.setPlaceholderText(_translate("GitAutocloner", "Please, enter GitHub repositories links, one link by one string (WITH PROTOCOL!)"))
        self.btn_clone.setText(_translate("GitAutocloner", "Clone!"))
        self.profile.setPlaceholderText(_translate("GitAutocloner", "GitHub username (or profile link with protocol)"))
        self.btn_clone_all.setText(_translate("GitAutocloner", "Clone!"))
        self.is_clone_all.setText(_translate("GitAutocloner", " Clone all repos\n"
" from account"))

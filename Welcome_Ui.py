# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Welcome.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Welcome(object):
    def setupUi(self, Welcome):
        if not Welcome.objectName():
            Welcome.setObjectName(u"Welcome")
        Welcome.resize(748, 586)
        Welcome.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.label = QLabel(Welcome)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 130, 251, 51))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.RightToLeft)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btn_Login = QPushButton(Welcome)
        self.btn_Login.setObjectName(u"btn_Login")
        self.btn_Login.setGeometry(QRect(180, 400, 101, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.btn_Login.setFont(font1)
        self.btn_Login.setStyleSheet(u"background-color: rgb(170, 161, 153);\n"
"color: rgb(0, 0, 0);")
        self.btn_Register = QPushButton(Welcome)
        self.btn_Register.setObjectName(u"btn_Register")
        self.btn_Register.setGeometry(QRect(480, 400, 101, 31))
        self.btn_Register.setFont(font1)
        self.btn_Register.setStyleSheet(u"background-color: rgb(170, 161, 153);\n"
"color: rgb(0, 0, 0);")

        self.retranslateUi(Welcome)

        QMetaObject.connectSlotsByName(Welcome)
    # setupUi

    def retranslateUi(self, Welcome):
        Welcome.setWindowTitle(QCoreApplication.translate("Welcome", u"Welcome", None))
        self.label.setText(QCoreApplication.translate("Welcome", u"Texi Booking System", None))
        self.btn_Login.setText(QCoreApplication.translate("Welcome", u"Login", None))
        self.btn_Register.setText(QCoreApplication.translate("Welcome", u"Register", None))
    # retranslateUi


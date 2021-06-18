# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(645, 453)
        font = QFont()
        font.setPointSize(12)
        Login.setFont(font)
        Login.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 50, 191, 41))
        font1 = QFont()
        font1.setPointSize(18)
        self.label.setFont(font1)
        self.txt_User = QTextEdit(Login)
        self.txt_User.setObjectName(u"txt_User")
        self.txt_User.setGeometry(QRect(200, 140, 381, 41))
        self.txt_User.setFont(font)
        self.txt_User.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_Password = QTextEdit(Login)
        self.txt_Password.setObjectName(u"txt_Password")
        self.txt_Password.setGeometry(QRect(200, 220, 381, 41))
        self.txt_Password.setFont(font)
        self.txt_Password.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(Login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 146, 101, 20))
        font2 = QFont()
        font2.setFamilies([u"MS UI Gothic"])
        font2.setPointSize(12)
        self.label_2.setFont(font2)
        self.label_3 = QLabel(Login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 230, 111, 20))
        self.label_3.setFont(font2)
        self.rAdmin = QRadioButton(Login)
        self.rAdmin.setObjectName(u"rAdmin")
        self.rAdmin.setGeometry(QRect(150, 290, 97, 22))
        self.rCustomer = QRadioButton(Login)
        self.rCustomer.setObjectName(u"rCustomer")
        self.rCustomer.setGeometry(QRect(290, 290, 97, 22))
        self.rDriver = QRadioButton(Login)
        self.rDriver.setObjectName(u"rDriver")
        self.rDriver.setGeometry(QRect(450, 290, 97, 22))
        self.btnlogin_window = QPushButton(Login)
        self.btnlogin_window.setObjectName(u"btnlogin_window")
        self.btnlogin_window.setGeometry(QRect(210, 350, 80, 25))
        font3 = QFont()
        font3.setPointSize(10)
        self.btnlogin_window.setFont(font3)
        self.btnlogin_window.setStyleSheet(u"background-color: rgb(255, 239, 226);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.btn_back = QPushButton(Login)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(450, 350, 80, 25))
        self.btn_back.setFont(font3)
        self.btn_back.setStyleSheet(u"background-color: rgb(255, 239, 226);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.Warninglbl = QLabel(Login)
        self.Warninglbl.setObjectName(u"Warninglbl")
        self.Warninglbl.setGeometry(QRect(270, 100, 131, 20))
        self.Warninglbl.setFont(font3)
        self.Warninglbl.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 3, 28);")
        self.Warninglbl.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.label.setText(QCoreApplication.translate("Login", u" Login User", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"USERNAME", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"PASSWORD", None))
        self.rAdmin.setText(QCoreApplication.translate("Login", u"Admin", None))
        self.rCustomer.setText(QCoreApplication.translate("Login", u"Cutomer", None))
        self.rDriver.setText(QCoreApplication.translate("Login", u"Driver", None))
        self.btnlogin_window.setText(QCoreApplication.translate("Login", u"Login", None))
        self.btn_back.setText(QCoreApplication.translate("Login", u"Back", None))
        self.Warninglbl.setText("")
    # retranslateUi


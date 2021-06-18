# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegisterDriver.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_RegisterDriver(object):
    def setupUi(self, RegisterDriver):
        if not RegisterDriver.objectName():
            RegisterDriver.setObjectName(u"RegisterDriver")
        RegisterDriver.resize(604, 706)
        RegisterDriver.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.formLayoutWidget = QWidget(RegisterDriver)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(110, 70, 421, 501))
        self.createaccForm = QFormLayout(self.formLayoutWidget)
        self.createaccForm.setObjectName(u"createaccForm")
        self.createaccForm.setContentsMargins(0, 0, 0, 0)
        self.acc_firstNameLabel = QLabel(self.formLayoutWidget)
        self.acc_firstNameLabel.setObjectName(u"acc_firstNameLabel")
        font = QFont()
        font.setFamilies([u"MS Gothic"])
        font.setPointSize(12)
        self.acc_firstNameLabel.setFont(font)
        self.acc_firstNameLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(0, QFormLayout.LabelRole, self.acc_firstNameLabel)

        self.txt_Tname = QLineEdit(self.formLayoutWidget)
        self.txt_Tname.setObjectName(u"txt_Tname")
        font1 = QFont()
        font1.setFamilies([u"Proxima Nova"])
        font1.setPointSize(12)
        self.txt_Tname.setFont(font1)
        self.txt_Tname.setStyleSheet(u"QLineEdit {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(120, 120, 120);\n"
"border:none;\n"
"border-radius: 5px;\n"
"padding-left: 10px;\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"}\n"
"QLineEdit::hover{\n"
"background-color: rgb(161, 161, 161);\n"
"}\n"
"QLineEdit::focus{\n"
"background-color: #474747\n"
"}")
        self.txt_Tname.setMaxLength(30)

        self.createaccForm.setWidget(0, QFormLayout.FieldRole, self.txt_Tname)

        self.acc_lastNameLabel = QLabel(self.formLayoutWidget)
        self.acc_lastNameLabel.setObjectName(u"acc_lastNameLabel")
        font2 = QFont()
        font2.setFamilies([u"MS PGothic"])
        font2.setPointSize(12)
        self.acc_lastNameLabel.setFont(font2)
        self.acc_lastNameLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(1, QFormLayout.LabelRole, self.acc_lastNameLabel)

        self.txt_Lname = QLineEdit(self.formLayoutWidget)
        self.txt_Lname.setObjectName(u"txt_Lname")
        self.txt_Lname.setFont(font1)
        self.txt_Lname.setStyleSheet(u"QLineEdit {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(120, 120, 120);\n"
"border:none;\n"
"border-radius: 5px;\n"
"padding-left: 10px;\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"}\n"
"QLineEdit::hover{\n"
"background-color: rgb(161, 161, 161);\n"
"}\n"
"QLineEdit::focus{\n"
"background-color: #474747\n"
"}")
        self.txt_Lname.setMaxLength(30)

        self.createaccForm.setWidget(1, QFormLayout.FieldRole, self.txt_Lname)

        self.acc_contactNoLabel = QLabel(self.formLayoutWidget)
        self.acc_contactNoLabel.setObjectName(u"acc_contactNoLabel")
        self.acc_contactNoLabel.setFont(font2)
        self.acc_contactNoLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(2, QFormLayout.LabelRole, self.acc_contactNoLabel)

        self.txt_Vno = QLineEdit(self.formLayoutWidget)
        self.txt_Vno.setObjectName(u"txt_Vno")
        self.txt_Vno.setFont(font1)
        self.txt_Vno.setStyleSheet(u"QLineEdit {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(120, 120, 120);\n"
"border:none;\n"
"border-radius: 5px;\n"
"padding-left: 10px;\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"}\n"
"QLineEdit::hover{\n"
"background-color: rgb(161, 161, 161);\n"
"}\n"
"QLineEdit::focus{\n"
"background-color: #474747\n"
"}")
        self.txt_Vno.setMaxLength(15)

        self.createaccForm.setWidget(2, QFormLayout.FieldRole, self.txt_Vno)

        self.acc_addressLabel = QLabel(self.formLayoutWidget)
        self.acc_addressLabel.setObjectName(u"acc_addressLabel")
        self.acc_addressLabel.setFont(font2)
        self.acc_addressLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(3, QFormLayout.LabelRole, self.acc_addressLabel)

        self.txt_Vtype = QLineEdit(self.formLayoutWidget)
        self.txt_Vtype.setObjectName(u"txt_Vtype")
        self.txt_Vtype.setFont(font1)
        self.txt_Vtype.setStyleSheet(u"QLineEdit {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(120, 120, 120);\n"
"border:none;\n"
"border-radius: 5px;\n"
"padding-left: 10px;\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"}\n"
"QLineEdit::hover{\n"
"background-color: rgb(161, 161, 161);\n"
"}\n"
"QLineEdit::focus{\n"
"background-color: #474747\n"
"}")
        self.txt_Vtype.setMaxLength(99)

        self.createaccForm.setWidget(3, QFormLayout.FieldRole, self.txt_Vtype)

        self.acc_emailLabel = QLabel(self.formLayoutWidget)
        self.acc_emailLabel.setObjectName(u"acc_emailLabel")
        self.acc_emailLabel.setFont(font2)
        self.acc_emailLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(4, QFormLayout.LabelRole, self.acc_emailLabel)

        self.tst_Psglt = QLineEdit(self.formLayoutWidget)
        self.tst_Psglt.setObjectName(u"tst_Psglt")
        self.tst_Psglt.setFont(font1)
        self.tst_Psglt.setStyleSheet(u"QLineEdit {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(120, 120, 120);\n"
"border:none;\n"
"border-radius: 5px;\n"
"padding-left: 10px;\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"}\n"
"QLineEdit::hover{\n"
"background-color: rgb(161, 161, 161);\n"
"}\n"
"QLineEdit::focus{\n"
"background-color: #474747\n"
"}")
        self.tst_Psglt.setMaxLength(50)

        self.createaccForm.setWidget(4, QFormLayout.FieldRole, self.tst_Psglt)

        self.acc_usernameLabel = QLabel(self.formLayoutWidget)
        self.acc_usernameLabel.setObjectName(u"acc_usernameLabel")
        self.acc_usernameLabel.setFont(font2)
        self.acc_usernameLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(5, QFormLayout.LabelRole, self.acc_usernameLabel)

        self.txt_username = QLineEdit(self.formLayoutWidget)
        self.txt_username.setObjectName(u"txt_username")
        self.txt_username.setFont(font1)
        self.txt_username.setStyleSheet(u"QLineEdit {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(120, 120, 120);\n"
"border:none;\n"
"border-radius: 5px;\n"
"padding-left: 10px;\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"}\n"
"QLineEdit::hover{\n"
"background-color: rgb(161, 161, 161);\n"
"}\n"
"QLineEdit::focus{\n"
"background-color: #474747\n"
"}")
        self.txt_username.setMaxLength(20)

        self.createaccForm.setWidget(5, QFormLayout.FieldRole, self.txt_username)

        self.acc_passwordLabel = QLabel(self.formLayoutWidget)
        self.acc_passwordLabel.setObjectName(u"acc_passwordLabel")
        self.acc_passwordLabel.setFont(font2)
        self.acc_passwordLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(6, QFormLayout.LabelRole, self.acc_passwordLabel)

        self.txt_pass = QLineEdit(self.formLayoutWidget)
        self.txt_pass.setObjectName(u"txt_pass")
        self.txt_pass.setFont(font1)
        self.txt_pass.setStyleSheet(u"QLineEdit {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(120, 120, 120);\n"
"border:none;\n"
"border-radius: 5px;\n"
"padding-left: 10px;\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"}\n"
"QLineEdit::hover{\n"
"background-color: rgb(161, 161, 161);\n"
"}\n"
"QLineEdit::focus{\n"
"background-color: #474747\n"
"}")
        self.txt_pass.setMaxLength(30)
        self.txt_pass.setEchoMode(QLineEdit.Password)

        self.createaccForm.setWidget(6, QFormLayout.FieldRole, self.txt_pass)

        self.acc_confirmPasswordLabel = QLabel(self.formLayoutWidget)
        self.acc_confirmPasswordLabel.setObjectName(u"acc_confirmPasswordLabel")
        self.acc_confirmPasswordLabel.setFont(font2)
        self.acc_confirmPasswordLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(7, QFormLayout.LabelRole, self.acc_confirmPasswordLabel)

        self.txt_conpass = QLineEdit(self.formLayoutWidget)
        self.txt_conpass.setObjectName(u"txt_conpass")
        self.txt_conpass.setFont(font1)
        self.txt_conpass.setStyleSheet(u"QLineEdit {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(120, 120, 120);\n"
"border:none;\n"
"border-radius: 5px;\n"
"padding-left: 10px;\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"}\n"
"QLineEdit::hover{\n"
"background-color: rgb(161, 161, 161);\n"
"}\n"
"QLineEdit::focus{\n"
"background-color: #474747\n"
"}")
        self.txt_conpass.setMaxLength(30)
        self.txt_conpass.setEchoMode(QLineEdit.Password)

        self.createaccForm.setWidget(7, QFormLayout.FieldRole, self.txt_conpass)

        self.label = QLabel(RegisterDriver)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 20, 321, 31))
        font3 = QFont()
        font3.setPointSize(14)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_Register = QPushButton(RegisterDriver)
        self.btn_Register.setObjectName(u"btn_Register")
        self.btn_Register.setGeometry(QRect(100, 600, 80, 25))
        font4 = QFont()
        font4.setPointSize(10)
        self.btn_Register.setFont(font4)
        self.btn_Register.setStyleSheet(u"background-color: rgb(255, 239, 226);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.btn_back = QPushButton(RegisterDriver)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(460, 600, 80, 25))
        self.btn_back.setFont(font4)
        self.btn_back.setStyleSheet(u"background-color: rgb(255, 239, 226);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.Warninglbl = QLabel(RegisterDriver)
        self.Warninglbl.setObjectName(u"Warninglbl")
        self.Warninglbl.setGeometry(QRect(210, 640, 211, 20))
        self.Warninglbl.setFont(font4)
        self.Warninglbl.setStyleSheet(u"color: rgb(255, 5, 38);\n"
"background-color: rgb(0, 0, 0);")
        self.Warninglbl.setAlignment(Qt.AlignCenter)

        self.retranslateUi(RegisterDriver)

        QMetaObject.connectSlotsByName(RegisterDriver)
    # setupUi

    def retranslateUi(self, RegisterDriver):
        RegisterDriver.setWindowTitle(QCoreApplication.translate("RegisterDriver", u"Frame", None))
        self.acc_firstNameLabel.setText(QCoreApplication.translate("RegisterDriver", u"First Name", None))
        self.acc_lastNameLabel.setText(QCoreApplication.translate("RegisterDriver", u"Last Name", None))
        self.acc_contactNoLabel.setText(QCoreApplication.translate("RegisterDriver", u"Vehicle No.", None))
        self.acc_addressLabel.setText(QCoreApplication.translate("RegisterDriver", u"Vehicle Type", None))
        self.acc_emailLabel.setText(QCoreApplication.translate("RegisterDriver", u"Passenger Limit", None))
        self.acc_usernameLabel.setText(QCoreApplication.translate("RegisterDriver", u"Username", None))
        self.acc_passwordLabel.setText(QCoreApplication.translate("RegisterDriver", u"Password", None))
        self.acc_confirmPasswordLabel.setText(QCoreApplication.translate("RegisterDriver", u"Confirm Password", None))
        self.label.setText(QCoreApplication.translate("RegisterDriver", u"Create Your Customer Account", None))
        self.btn_Register.setText(QCoreApplication.translate("RegisterDriver", u"Register", None))
        self.btn_back.setText(QCoreApplication.translate("RegisterDriver", u"Back", None))
        self.Warninglbl.setText("")
    # retranslateUi


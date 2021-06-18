# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Register.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Register(object):
    def setupUi(self, Register):
        if not Register.objectName():
            Register.setObjectName(u"Register")
        Register.resize(606, 736)
        Register.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.formLayoutWidget = QWidget(Register)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(70, 60, 451, 556))
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

        self.acc_firstNameField = QLineEdit(self.formLayoutWidget)
        self.acc_firstNameField.setObjectName(u"acc_firstNameField")
        font1 = QFont()
        font1.setFamilies([u"Proxima Nova"])
        font1.setPointSize(12)
        self.acc_firstNameField.setFont(font1)
        self.acc_firstNameField.setStyleSheet(u"QLineEdit {\n"
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
        self.acc_firstNameField.setMaxLength(30)

        self.createaccForm.setWidget(0, QFormLayout.FieldRole, self.acc_firstNameField)

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

        self.acc_lastNameField = QLineEdit(self.formLayoutWidget)
        self.acc_lastNameField.setObjectName(u"acc_lastNameField")
        self.acc_lastNameField.setFont(font1)
        self.acc_lastNameField.setStyleSheet(u"QLineEdit {\n"
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
        self.acc_lastNameField.setMaxLength(30)

        self.createaccForm.setWidget(1, QFormLayout.FieldRole, self.acc_lastNameField)

        self.acc_contactNoLabel = QLabel(self.formLayoutWidget)
        self.acc_contactNoLabel.setObjectName(u"acc_contactNoLabel")
        self.acc_contactNoLabel.setFont(font2)
        self.acc_contactNoLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(2, QFormLayout.LabelRole, self.acc_contactNoLabel)

        self.acc_contactNoField = QLineEdit(self.formLayoutWidget)
        self.acc_contactNoField.setObjectName(u"acc_contactNoField")
        self.acc_contactNoField.setFont(font1)
        self.acc_contactNoField.setStyleSheet(u"QLineEdit {\n"
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
        self.acc_contactNoField.setMaxLength(15)

        self.createaccForm.setWidget(2, QFormLayout.FieldRole, self.acc_contactNoField)

        self.acc_addressLabel = QLabel(self.formLayoutWidget)
        self.acc_addressLabel.setObjectName(u"acc_addressLabel")
        self.acc_addressLabel.setFont(font2)
        self.acc_addressLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(3, QFormLayout.LabelRole, self.acc_addressLabel)

        self.acc_addressField = QLineEdit(self.formLayoutWidget)
        self.acc_addressField.setObjectName(u"acc_addressField")
        self.acc_addressField.setFont(font1)
        self.acc_addressField.setStyleSheet(u"QLineEdit {\n"
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
        self.acc_addressField.setMaxLength(99)

        self.createaccForm.setWidget(3, QFormLayout.FieldRole, self.acc_addressField)

        self.acc_emailLabel = QLabel(self.formLayoutWidget)
        self.acc_emailLabel.setObjectName(u"acc_emailLabel")
        self.acc_emailLabel.setFont(font2)
        self.acc_emailLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(4, QFormLayout.LabelRole, self.acc_emailLabel)

        self.acc_emailField = QLineEdit(self.formLayoutWidget)
        self.acc_emailField.setObjectName(u"acc_emailField")
        self.acc_emailField.setFont(font1)
        self.acc_emailField.setStyleSheet(u"QLineEdit {\n"
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
        self.acc_emailField.setMaxLength(50)

        self.createaccForm.setWidget(4, QFormLayout.FieldRole, self.acc_emailField)

        self.acc_usernameLabel = QLabel(self.formLayoutWidget)
        self.acc_usernameLabel.setObjectName(u"acc_usernameLabel")
        self.acc_usernameLabel.setFont(font2)
        self.acc_usernameLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(5, QFormLayout.LabelRole, self.acc_usernameLabel)

        self.acc_usernameField = QLineEdit(self.formLayoutWidget)
        self.acc_usernameField.setObjectName(u"acc_usernameField")
        self.acc_usernameField.setFont(font1)
        self.acc_usernameField.setStyleSheet(u"QLineEdit {\n"
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
        self.acc_usernameField.setMaxLength(20)

        self.createaccForm.setWidget(5, QFormLayout.FieldRole, self.acc_usernameField)

        self.acc_passwordLabel = QLabel(self.formLayoutWidget)
        self.acc_passwordLabel.setObjectName(u"acc_passwordLabel")
        self.acc_passwordLabel.setFont(font2)
        self.acc_passwordLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(6, QFormLayout.LabelRole, self.acc_passwordLabel)

        self.acc_passwordField = QLineEdit(self.formLayoutWidget)
        self.acc_passwordField.setObjectName(u"acc_passwordField")
        self.acc_passwordField.setFont(font1)
        self.acc_passwordField.setStyleSheet(u"QLineEdit {\n"
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
        self.acc_passwordField.setMaxLength(30)
        self.acc_passwordField.setEchoMode(QLineEdit.Password)

        self.createaccForm.setWidget(6, QFormLayout.FieldRole, self.acc_passwordField)

        self.acc_confirmPasswordLabel = QLabel(self.formLayoutWidget)
        self.acc_confirmPasswordLabel.setObjectName(u"acc_confirmPasswordLabel")
        self.acc_confirmPasswordLabel.setFont(font2)
        self.acc_confirmPasswordLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(7, QFormLayout.LabelRole, self.acc_confirmPasswordLabel)

        self.acc_confirmPasswordField = QLineEdit(self.formLayoutWidget)
        self.acc_confirmPasswordField.setObjectName(u"acc_confirmPasswordField")
        self.acc_confirmPasswordField.setFont(font1)
        self.acc_confirmPasswordField.setStyleSheet(u"QLineEdit {\n"
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
        self.acc_confirmPasswordField.setMaxLength(30)
        self.acc_confirmPasswordField.setEchoMode(QLineEdit.Password)

        self.createaccForm.setWidget(7, QFormLayout.FieldRole, self.acc_confirmPasswordField)

        self.acc_confirmPasswordLabel_6 = QLabel(self.formLayoutWidget)
        self.acc_confirmPasswordLabel_6.setObjectName(u"acc_confirmPasswordLabel_6")
        self.acc_confirmPasswordLabel_6.setFont(font2)
        self.acc_confirmPasswordLabel_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(8, QFormLayout.LabelRole, self.acc_confirmPasswordLabel_6)

        self.comboBox = QComboBox(self.formLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        font3 = QFont()
        font3.setPointSize(10)
        self.comboBox.setFont(font3)
        self.comboBox.setStyleSheet(u"background-color: rgb(157, 157, 157);\n"
"color: rgb(0, 0, 0);")

        self.createaccForm.setWidget(8, QFormLayout.FieldRole, self.comboBox)

        self.label = QLabel(Register)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 20, 321, 31))
        font4 = QFont()
        font4.setPointSize(14)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_Register = QPushButton(Register)
        self.btn_Register.setObjectName(u"btn_Register")
        self.btn_Register.setGeometry(QRect(50, 680, 80, 25))
        self.btn_Register.setFont(font3)
        self.btn_Register.setStyleSheet(u"background-color: rgb(255, 239, 226);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.btn_back = QPushButton(Register)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(460, 680, 80, 25))
        self.btn_back.setFont(font3)
        self.btn_back.setStyleSheet(u"background-color: rgb(255, 239, 226);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.Warninglbl = QLabel(Register)
        self.Warninglbl.setObjectName(u"Warninglbl")
        self.Warninglbl.setGeometry(QRect(200, 700, 211, 20))
        self.Warninglbl.setFont(font3)
        self.Warninglbl.setStyleSheet(u"color: rgb(255, 5, 38);\n"
"background-color: rgb(0, 0, 0);")
        self.Warninglbl.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"Frame", None))
        self.acc_firstNameLabel.setText(QCoreApplication.translate("Register", u"First Name", None))
        self.acc_lastNameLabel.setText(QCoreApplication.translate("Register", u"Last Name", None))
        self.acc_contactNoLabel.setText(QCoreApplication.translate("Register", u"Contact No.", None))
        self.acc_addressLabel.setText(QCoreApplication.translate("Register", u"Address", None))
        self.acc_emailLabel.setText(QCoreApplication.translate("Register", u"Email", None))
        self.acc_usernameLabel.setText(QCoreApplication.translate("Register", u"Username", None))
        self.acc_passwordLabel.setText(QCoreApplication.translate("Register", u"Password", None))
        self.acc_confirmPasswordLabel.setText(QCoreApplication.translate("Register", u"Confirm Password", None))
        self.acc_confirmPasswordLabel_6.setText(QCoreApplication.translate("Register", u"Payment Method", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Register", u"Cash on Delivery", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Register", u"Master Card", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Register", u"Visa Card", None))

        self.label.setText(QCoreApplication.translate("Register", u"Create Your Customer Account", None))
        self.btn_Register.setText(QCoreApplication.translate("Register", u"Register", None))
        self.btn_back.setText(QCoreApplication.translate("Register", u"Back", None))
        self.Warninglbl.setText("")
    # retranslateUi


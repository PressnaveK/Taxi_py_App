# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DriverBooking.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_DriverBooking(object):
    def setupUi(self, DriverBooking):
        if not DriverBooking.objectName():
            DriverBooking.setObjectName(u"DriverBooking")
        DriverBooking.resize(604, 706)
        DriverBooking.setStyleSheet(u"background-color: rgb(0, 0, 0);color: rgb(255,255,255);")
        self.formLayoutWidget = QWidget(DriverBooking)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(110, 70, 421, 481))
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

        self.txt_Driver = QComboBox(self.formLayoutWidget)
        self.txt_Driver.setObjectName(u"txt_Driver")
        font1 = QFont()
        font1.setPointSize(10)
        self.txt_Driver.setFont(font1)
        self.txt_Driver.setStyleSheet(u"background-color: rgb(141, 141, 141);\n"
"color: rgb(0,0,0);selection-background-color: rgb(255, 0, 0);alternate-background-color: rgb(255, 255, 255);")




        self.createaccForm.setWidget(0, QFormLayout.FieldRole, self.txt_Driver)

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

        self.txt_pick = QLineEdit(self.formLayoutWidget)
        self.txt_pick.setObjectName(u"txt_pick")
        font3 = QFont()
        font3.setFamilies([u"Proxima Nova"])
        font3.setPointSize(12)
        self.txt_pick.setFont(font3)
        self.txt_pick.setStyleSheet(u"QLineEdit {\n"
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
        self.txt_pick.setMaxLength(30)

        self.createaccForm.setWidget(1, QFormLayout.FieldRole, self.txt_pick)

        self.acc_contactNoLabel = QLabel(self.formLayoutWidget)
        self.acc_contactNoLabel.setObjectName(u"acc_contactNoLabel")
        self.acc_contactNoLabel.setFont(font2)
        self.acc_contactNoLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(2, QFormLayout.LabelRole, self.acc_contactNoLabel)

        self.txt_dist = QLineEdit(self.formLayoutWidget)
        self.txt_dist.setObjectName(u"txt_dist")
        self.txt_dist.setFont(font3)
        self.txt_dist.setStyleSheet(u"QLineEdit {\n"
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
        self.txt_dist.setMaxLength(15)

        self.createaccForm.setWidget(2, QFormLayout.FieldRole, self.txt_dist)

        self.acc_addressLabel = QLabel(self.formLayoutWidget)
        self.acc_addressLabel.setObjectName(u"acc_addressLabel")
        self.acc_addressLabel.setFont(font2)
        self.acc_addressLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(3, QFormLayout.LabelRole, self.acc_addressLabel)

        self.txtDate_P = QDateEdit(self.formLayoutWidget)
        self.txtDate_P.setObjectName(u"txtDate_P")
        font4 = QFont()
        font4.setPointSize(12)
        self.txtDate_P.setFont(font4)
        self.txtDate_P.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(255, 255, 255);")
        self.txtDate_P.setAlignment(Qt.AlignCenter)

        self.createaccForm.setWidget(3, QFormLayout.FieldRole, self.txtDate_P)

        self.acc_emailLabel = QLabel(self.formLayoutWidget)
        self.acc_emailLabel.setObjectName(u"acc_emailLabel")
        self.acc_emailLabel.setFont(font2)
        self.acc_emailLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(4, QFormLayout.LabelRole, self.acc_emailLabel)

        self.txtTime_P = QTimeEdit(self.formLayoutWidget)
        self.txtTime_P.setObjectName(u"txtTime_P")
        self.txtTime_P.setFont(font4)
        self.txtTime_P.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(255, 255, 255);")
        self.txtTime_P.setAlignment(Qt.AlignCenter)

        self.createaccForm.setWidget(4, QFormLayout.FieldRole, self.txtTime_P)

        self.txtDate_B = QDateEdit(self.formLayoutWidget)
        self.txtDate_B.setObjectName(u"txtDate_B")
        self.txtDate_B.setFont(font4)
        self.txtDate_B.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(255, 255, 255);")
        self.txtDate_B.setAlignment(Qt.AlignCenter)

        self.createaccForm.setWidget(5, QFormLayout.FieldRole, self.txtDate_B)

        self.acc_usernameLabel = QLabel(self.formLayoutWidget)
        self.acc_usernameLabel.setObjectName(u"acc_usernameLabel")
        self.acc_usernameLabel.setFont(font2)
        self.acc_usernameLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(5, QFormLayout.LabelRole, self.acc_usernameLabel)

        self.txtTime_B = QTimeEdit(self.formLayoutWidget)
        self.txtTime_B.setObjectName(u"txtTime_B")
        self.txtTime_B.setFont(font4)
        self.txtTime_B.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(255, 255, 255);")
        self.txtTime_B.setAlignment(Qt.AlignCenter)

        self.createaccForm.setWidget(6, QFormLayout.FieldRole, self.txtTime_B)

        self.acc_passwordLabel = QLabel(self.formLayoutWidget)
        self.acc_passwordLabel.setObjectName(u"acc_passwordLabel")
        self.acc_passwordLabel.setFont(font2)
        self.acc_passwordLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(6, QFormLayout.LabelRole, self.acc_passwordLabel)

        self.txt_Passenger = QLineEdit(self.formLayoutWidget)
        self.txt_Passenger.setObjectName(u"txt_Passenger")
        self.txt_Passenger.setFont(font3)
        self.txt_Passenger.setStyleSheet(u"QLineEdit {\n"
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
        self.txt_Passenger.setMaxLength(30)
        self.txt_Passenger.setEchoMode(QLineEdit.Password)

        self.createaccForm.setWidget(7, QFormLayout.FieldRole, self.txt_Passenger)

        self.acc_confirmPasswordLabel = QLabel(self.formLayoutWidget)
        self.acc_confirmPasswordLabel.setObjectName(u"acc_confirmPasswordLabel")
        self.acc_confirmPasswordLabel.setFont(font2)
        self.acc_confirmPasswordLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-bottom:20px;\n"
"margin-top:10px;\n"
"\n"
"")

        self.createaccForm.setWidget(7, QFormLayout.LabelRole, self.acc_confirmPasswordLabel)

        self.label = QLabel(DriverBooking)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 20, 91, 31))
        font5 = QFont()
        font5.setPointSize(14)
        self.label.setFont(font5)
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_Book = QPushButton(DriverBooking)
        self.btn_Book.setObjectName(u"btn_Book")
        self.btn_Book.setGeometry(QRect(100, 600, 80, 25))
        self.btn_Book.setFont(font1)
        self.btn_Book.setStyleSheet(u"background-color: rgb(255, 239, 226);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.btn_back = QPushButton(DriverBooking)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(460, 600, 80, 25))
        self.btn_back.setFont(font1)
        self.btn_back.setStyleSheet(u"background-color: rgb(255, 239, 226);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.Warninglbl = QLabel(DriverBooking)
        self.Warninglbl.setObjectName(u"Warninglbl")
        self.Warninglbl.setGeometry(QRect(210, 640, 211, 20))
        self.Warninglbl.setFont(font1)
        self.Warninglbl.setStyleSheet(u"color: rgb(255, 5, 38);\n"
"background-color: rgb(0, 0, 0);")
        self.Warninglbl.setAlignment(Qt.AlignCenter)

        self.retranslateUi(DriverBooking)

        QMetaObject.connectSlotsByName(DriverBooking)
    # setupUi

    def retranslateUi(self, DriverBooking):
        DriverBooking.setWindowTitle(QCoreApplication.translate("DriverBooking", u"Frame", None))
        self.acc_firstNameLabel.setText(QCoreApplication.translate("DriverBooking", u"Driver Name", None))
        self.acc_lastNameLabel.setText(QCoreApplication.translate("DriverBooking", u"Pickup", None))
        self.acc_contactNoLabel.setText(QCoreApplication.translate("DriverBooking", u"Destination", None))
        self.acc_addressLabel.setText(QCoreApplication.translate("DriverBooking", u"Pickup Date", None))
        self.acc_emailLabel.setText(QCoreApplication.translate("DriverBooking", u"Pickup Time", None))
        self.acc_usernameLabel.setText(QCoreApplication.translate("DriverBooking", u"Booking Date", None))
        self.acc_passwordLabel.setText(QCoreApplication.translate("DriverBooking", u"Booking Time", None))
        self.acc_confirmPasswordLabel.setText(QCoreApplication.translate("DriverBooking", u"No of Passenger", None))
        self.label.setText(QCoreApplication.translate("DriverBooking", u"Bookings", None))
        self.btn_Book.setText(QCoreApplication.translate("DriverBooking", u"Book", None))
        self.btn_back.setText(QCoreApplication.translate("DriverBooking", u"Back", None))
        self.Warninglbl.setText("")
    # retranslateUi


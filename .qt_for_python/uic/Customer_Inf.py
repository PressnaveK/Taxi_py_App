# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Customer_Inf.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Customer_Inf(object):
    def setupUi(self, Customer_Inf):
        if not Customer_Inf.objectName():
            Customer_Inf.setObjectName(u"Customer_Inf")
        Customer_Inf.resize(739, 290)
        font = QFont()
        font.setPointSize(9)
        Customer_Inf.setFont(font)
        Customer_Inf.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.label = QLabel(Customer_Inf)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 10, 291, 31))
        font1 = QFont()
        font1.setPointSize(16)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btnBook = QPushButton(Customer_Inf)
        self.btnBook.setObjectName(u"btnBook")
        self.btnBook.setGeometry(QRect(140, 180, 121, 41))
        font2 = QFont()
        font2.setPointSize(10)
        self.btnBook.setFont(font2)
        self.btnBook.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(132, 121, 115);")
        self.btnBookingInfo = QPushButton(Customer_Inf)
        self.btnBookingInfo.setObjectName(u"btnBookingInfo")
        self.btnBookingInfo.setGeometry(QRect(320, 180, 121, 41))
        self.btnBookingInfo.setFont(font2)
        self.btnBookingInfo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(132, 121, 115);")
        self.btnPay = QPushButton(Customer_Inf)
        self.btnPay.setObjectName(u"btnPay")
        self.btnPay.setGeometry(QRect(500, 180, 121, 41))
        self.btnPay.setFont(font2)
        self.btnPay.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(132, 121, 115);")
        self.label_2 = QLabel(Customer_Inf)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 96, 741, 20))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.lbl_User = QLabel(Customer_Inf)
        self.lbl_User.setObjectName(u"lbl_User")
        self.lbl_User.setGeometry(QRect(0, 120, 741, 41))
        font3 = QFont()
        font3.setPointSize(12)
        self.lbl_User.setFont(font3)
        self.lbl_User.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.lbl_User.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Customer_Inf)

        QMetaObject.connectSlotsByName(Customer_Inf)
    # setupUi

    def retranslateUi(self, Customer_Inf):
        Customer_Inf.setWindowTitle(QCoreApplication.translate("Customer_Inf", u"Frame", None))
        self.label.setText(QCoreApplication.translate("Customer_Inf", u"CUSTOMER INTERFACE", None))
        self.btnBook.setText(QCoreApplication.translate("Customer_Inf", u"Book", None))
        self.btnBookingInfo.setText(QCoreApplication.translate("Customer_Inf", u"Booking Info", None))
        self.btnPay.setText(QCoreApplication.translate("Customer_Inf", u"Pay", None))
        self.label_2.setText(QCoreApplication.translate("Customer_Inf", u"Logged In User", None))
        self.lbl_User.setText("")
    # retranslateUi


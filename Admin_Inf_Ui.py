# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Admin_Inf.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Admin_Inf(object):
    def setupUi(self, Admin_Inf):
        if not Admin_Inf.objectName():
            Admin_Inf.setObjectName(u"Admin_Inf")
        Admin_Inf.resize(739, 290)
        font = QFont()
        font.setPointSize(9)
        Admin_Inf.setFont(font)
        Admin_Inf.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.label = QLabel(Admin_Inf)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 10, 231, 31))
        font1 = QFont()
        font1.setPointSize(16)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btnCustomerInfo = QPushButton(Admin_Inf)
        self.btnCustomerInfo.setObjectName(u"btnCustomerInfo")
        self.btnCustomerInfo.setGeometry(QRect(110, 180, 121, 41))
        font2 = QFont()
        font2.setPointSize(10)
        self.btnCustomerInfo.setFont(font2)
        self.btnCustomerInfo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(132, 121, 115);")
        self.btnDriverInfo = QPushButton(Admin_Inf)
        self.btnDriverInfo.setObjectName(u"btnDriverInfo")
        self.btnDriverInfo.setGeometry(QRect(240, 180, 121, 41))
        self.btnDriverInfo.setFont(font2)
        self.btnDriverInfo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(132, 121, 115);")
        self.btnBookingInfo = QPushButton(Admin_Inf)
        self.btnBookingInfo.setObjectName(u"btnBookingInfo")
        self.btnBookingInfo.setGeometry(QRect(370, 180, 121, 41))
        self.btnBookingInfo.setFont(font2)
        self.btnBookingInfo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(132, 121, 115);")
        self.btnRegDrivers = QPushButton(Admin_Inf)
        self.btnRegDrivers.setObjectName(u"btnRegDrivers")
        self.btnRegDrivers.setGeometry(QRect(500, 180, 121, 41))
        self.btnRegDrivers.setFont(font)
        self.btnRegDrivers.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(132, 121, 115);")
        self.label_2 = QLabel(Admin_Inf)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 76, 741, 20))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.lbl_User = QLabel(Admin_Inf)
        self.lbl_User.setObjectName(u"lbl_User")
        self.lbl_User.setGeometry(QRect(0, 100, 741, 41))
        font3 = QFont()
        font3.setPointSize(12)
        self.lbl_User.setFont(font3)
        self.lbl_User.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.lbl_User.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Admin_Inf)

        QMetaObject.connectSlotsByName(Admin_Inf)
    # setupUi

    def retranslateUi(self, Admin_Inf):
        Admin_Inf.setWindowTitle(QCoreApplication.translate("Admin_Inf", u"Frame", None))
        self.label.setText(QCoreApplication.translate("Admin_Inf", u"ADMIN INTERFACE", None))
        self.btnCustomerInfo.setText(QCoreApplication.translate("Admin_Inf", u"Customer Info", None))
        self.btnDriverInfo.setText(QCoreApplication.translate("Admin_Inf", u"Driver Info", None))
        self.btnBookingInfo.setText(QCoreApplication.translate("Admin_Inf", u"Booking Info", None))
        self.btnRegDrivers.setText(QCoreApplication.translate("Admin_Inf", u"Register Drivers", None))
        self.label_2.setText(QCoreApplication.translate("Admin_Inf", u"Logged In User", None))
        self.lbl_User.setText("")
    # retranslateUi


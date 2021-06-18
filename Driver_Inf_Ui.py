# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Driver_Inf.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Driver_Inf(object):
    def setupUi(self, Driver_Inf):
        if not Driver_Inf.objectName():
            Driver_Inf.setObjectName(u"Driver_Inf")
        Driver_Inf.resize(739, 290)
        font = QFont()
        font.setPointSize(9)
        Driver_Inf.setFont(font)
        Driver_Inf.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.label = QLabel(Driver_Inf)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 10, 291, 31))
        font1 = QFont()
        font1.setPointSize(16)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btnBooking_info = QPushButton(Driver_Inf)
        self.btnBooking_info.setObjectName(u"btnBooking_info")
        self.btnBooking_info.setGeometry(QRect(140, 180, 121, 41))
        font2 = QFont()
        font2.setPointSize(10)
        self.btnBooking_info.setFont(font2)
        self.btnBooking_info.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(132, 121, 115);")
        self.btnConfirm = QPushButton(Driver_Inf)
        self.btnConfirm.setObjectName(u"btnConfirm")
        self.btnConfirm.setGeometry(QRect(500, 180, 121, 41))
        self.btnConfirm.setFont(font2)
        self.btnConfirm.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(132, 121, 115);")
        self.label_2 = QLabel(Driver_Inf)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 106, 741, 20))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.lbl_User = QLabel(Driver_Inf)
        self.lbl_User.setObjectName(u"lbl_User")
        self.lbl_User.setGeometry(QRect(0, 130, 741, 41))
        font3 = QFont()
        font3.setPointSize(12)
        self.lbl_User.setFont(font3)
        self.lbl_User.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.lbl_User.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Driver_Inf)

        QMetaObject.connectSlotsByName(Driver_Inf)
    # setupUi

    def retranslateUi(self, Driver_Inf):
        Driver_Inf.setWindowTitle(QCoreApplication.translate("Driver_Inf", u"Frame", None))
        self.label.setText(QCoreApplication.translate("Driver_Inf", u"DRIVER INTERFACE", None))
        self.btnBooking_info.setText(QCoreApplication.translate("Driver_Inf", u"Booking Info", None))
        self.btnConfirm.setText(QCoreApplication.translate("Driver_Inf", u"Confirm", None))
        self.label_2.setText(QCoreApplication.translate("Driver_Inf", u"Logged In User", None))
        self.lbl_User.setText("")
    # retranslateUi


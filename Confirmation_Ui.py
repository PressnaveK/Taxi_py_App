# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Confirmation.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Confirmation(object):
    def setupUi(self, Confirmation):
        if not Confirmation.objectName():
            Confirmation.setObjectName(u"Confirmation")
        Confirmation.resize(489, 375)
        Confirmation.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label = QLabel(Confirmation)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 36, 491, 31))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.txt_ID = QComboBox(Confirmation)
        self.txt_ID.setObjectName(u"txt_ID")
        self.txt_ID.setGeometry(QRect(230, 80, 171, 41))
        self.txt_ID.setStyleSheet(u"background-color: rgb(76, 76, 76);\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(Confirmation)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 70, 121, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbl_Customer = QLabel(Confirmation)
        self.lbl_Customer.setObjectName(u"lbl_Customer")
        self.lbl_Customer.setGeometry(QRect(0, 160, 491, 20))
        font2 = QFont()
        font2.setPointSize(10)
        self.lbl_Customer.setFont(font2)
        self.lbl_Customer.setStyleSheet(u"color: rgb(170, 0, 0);")
        self.lbl_Customer.setAlignment(Qt.AlignCenter)
        self.btn_pay = QPushButton(Confirmation)
        self.btn_pay.setObjectName(u"btn_pay")
        self.btn_pay.setGeometry(QRect(60, 290, 80, 25))
        self.btn_pay.setFont(font2)
        self.btn_pay.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"color: rgb(0, 0, 0);")
        self.btn_back = QPushButton(Confirmation)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(350, 290, 80, 25))
        self.btn_back.setFont(font2)
        self.btn_back.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"color: rgb(0, 0, 0);")
        self.txt_Payment = QLineEdit(Confirmation)
        self.txt_Payment.setObjectName(u"txt_Payment")
        self.txt_Payment.setGeometry(QRect(230, 220, 171, 41))
        self.txt_Payment.setFont(font2)
        self.txt_Payment.setStyleSheet(u"background-color: rgb(76, 76, 76);\n"
"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(Confirmation)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 220, 121, 41))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(Confirmation)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 120, 491, 41))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Confirmation)

        QMetaObject.connectSlotsByName(Confirmation)
    # setupUi

    def retranslateUi(self, Confirmation):
        Confirmation.setWindowTitle(QCoreApplication.translate("Confirmation", u"Frame", None))
        self.label.setText(QCoreApplication.translate("Confirmation", u"Confirmation", None))
        self.label_2.setText(QCoreApplication.translate("Confirmation", u"Booking ID", None))
        self.lbl_Customer.setText("")
        self.btn_pay.setText(QCoreApplication.translate("Confirmation", u"Pay", None))
        self.btn_back.setText(QCoreApplication.translate("Confirmation", u"Back", None))
        self.label_3.setText(QCoreApplication.translate("Confirmation", u"Payment", None))
        self.label_4.setText(QCoreApplication.translate("Confirmation", u"Customer Name", None))
    # retranslateUi


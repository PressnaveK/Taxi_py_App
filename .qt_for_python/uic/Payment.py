# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Payment.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Payment(object):
    def setupUi(self, Payment):
        if not Payment.objectName():
            Payment.setObjectName(u"Payment")
        Payment.resize(489, 375)
        Payment.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label = QLabel(Payment)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 36, 491, 31))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.txt_ID = QComboBox(Payment)
        self.txt_ID.setObjectName(u"txt_ID")
        self.txt_ID.setGeometry(QRect(230, 90, 171, 41))
        self.txt_ID.setStyleSheet(u"background-color: rgb(76, 76, 76);\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(Payment)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 90, 121, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbl_Driver = QLabel(Payment)
        self.lbl_Driver.setObjectName(u"lbl_Driver")
        self.lbl_Driver.setGeometry(QRect(0, 170, 491, 20))
        font2 = QFont()
        font2.setPointSize(10)
        self.lbl_Driver.setFont(font2)
        self.lbl_Driver.setStyleSheet(u"color: rgb(170, 0, 0);")
        self.lbl_Driver.setAlignment(Qt.AlignCenter)
        self.lbl_Payment = QLabel(Payment)
        self.lbl_Payment.setObjectName(u"lbl_Payment")
        self.lbl_Payment.setGeometry(QRect(0, 230, 491, 20))
        self.lbl_Payment.setFont(font2)
        self.lbl_Payment.setStyleSheet(u"color: rgb(170, 0, 0);")
        self.lbl_Payment.setAlignment(Qt.AlignCenter)
        self.btn_pay = QPushButton(Payment)
        self.btn_pay.setObjectName(u"btn_pay")
        self.btn_pay.setGeometry(QRect(60, 270, 80, 25))
        self.btn_pay.setFont(font2)
        self.btn_pay.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"color: rgb(0, 0, 0);")
        self.btn_back = QPushButton(Payment)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(340, 270, 80, 25))
        self.btn_back.setFont(font2)
        self.btn_back.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"color: rgb(0, 0, 0);")
        self.label_4 = QLabel(Payment)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 130, 491, 41))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(Payment)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 190, 491, 41))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Payment)

        QMetaObject.connectSlotsByName(Payment)
    # setupUi

    def retranslateUi(self, Payment):
        Payment.setWindowTitle(QCoreApplication.translate("Payment", u"Frame", None))
        self.label.setText(QCoreApplication.translate("Payment", u"Payment", None))
        self.label_2.setText(QCoreApplication.translate("Payment", u"Booking ID", None))
        self.lbl_Driver.setText("")
        self.lbl_Payment.setText("")
        self.btn_pay.setText(QCoreApplication.translate("Payment", u"Pay", None))
        self.btn_back.setText(QCoreApplication.translate("Payment", u"Back", None))
        self.label_4.setText(QCoreApplication.translate("Payment", u"Customer Name", None))
        self.label_5.setText(QCoreApplication.translate("Payment", u"Charged", None))
    # retranslateUi


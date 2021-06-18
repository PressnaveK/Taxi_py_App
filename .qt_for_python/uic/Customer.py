# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Customer.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Customer(object):
    def setupUi(self, Customer):
        if not Customer.objectName():
            Customer.setObjectName(u"Customer")
        Customer.resize(1054, 699)
        Customer.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.vb_widget = QTableWidget(Customer)
        if (self.vb_widget.columnCount() < 7):
            self.vb_widget.setColumnCount(7)
        font = QFont()
        font.setFamilies([u"Proxima Nova"])
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.vb_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.vb_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.vb_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.vb_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.vb_widget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.vb_widget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.vb_widget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.vb_widget.setObjectName(u"vb_widget")
        self.vb_widget.setGeometry(QRect(140, 110, 771, 521))
        self.vb_widget.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(0, 0, 0);\n"
"border-color: rgb(11, 11, 11);\n"
"background-color: rgb(144, 144, 144);")
        self.label = QLabel(Customer)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(420, 60, 281, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_back = QPushButton(Customer)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(820, 50, 80, 25))
        font2 = QFont()
        font2.setPointSize(10)
        self.btn_back.setFont(font2)
        self.btn_back.setStyleSheet(u"background-color: rgb(148, 148, 148);\n"
"color: rgb(0, 0, 0);")

        self.retranslateUi(Customer)

        QMetaObject.connectSlotsByName(Customer)
    # setupUi

    def retranslateUi(self, Customer):
        Customer.setWindowTitle(QCoreApplication.translate("Customer", u"Frame", None))
        ___qtablewidgetitem = self.vb_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Customer", u"Username", None));
        ___qtablewidgetitem1 = self.vb_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Customer", u"Password", None));
        ___qtablewidgetitem2 = self.vb_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Customer", u"First_Name", None));
        ___qtablewidgetitem3 = self.vb_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Customer", u"Last_Name", None));
        ___qtablewidgetitem4 = self.vb_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Customer", u"Phone No", None));
        ___qtablewidgetitem5 = self.vb_widget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Customer", u"Email", None));
        ___qtablewidgetitem6 = self.vb_widget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Customer", u"Address", None));
        self.label.setText(QCoreApplication.translate("Customer", u"Customer Info", None))
        self.btn_back.setText(QCoreApplication.translate("Customer", u"Back", None))
    # retranslateUi


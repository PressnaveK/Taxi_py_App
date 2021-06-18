# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Driver.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Driver(object):
    def setupUi(self, Driver):
        if not Driver.objectName():
            Driver.setObjectName(u"Driver")
        Driver.resize(1054, 699)
        Driver.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.vb_widget = QTableWidget(Driver)
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
        self.label = QLabel(Driver)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(420, 60, 281, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_back = QPushButton(Driver)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(820, 50, 80, 25))
        font2 = QFont()
        font2.setPointSize(10)
        self.btn_back.setFont(font2)
        self.btn_back.setStyleSheet(u"background-color: rgb(148, 148, 148);\n"
"color: rgb(0, 0, 0);")

        self.retranslateUi(Driver)

        QMetaObject.connectSlotsByName(Driver)
    # setupUi

    def retranslateUi(self, Driver):
        Driver.setWindowTitle(QCoreApplication.translate("Driver", u"Frame", None))
        ___qtablewidgetitem = self.vb_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Driver", u"Username", None));
        ___qtablewidgetitem1 = self.vb_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Driver", u"Password", None));
        ___qtablewidgetitem2 = self.vb_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Driver", u"First_Name", None));
        ___qtablewidgetitem3 = self.vb_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Driver", u"Last_Name", None));
        ___qtablewidgetitem4 = self.vb_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Driver", u"Vehicle_Type", None));
        ___qtablewidgetitem5 = self.vb_widget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Driver", u"Passenger lim", None));
        ___qtablewidgetitem6 = self.vb_widget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Driver", u"Vehicle_No", None));
        self.label.setText(QCoreApplication.translate("Driver", u"Driver Info", None))
        self.btn_back.setText(QCoreApplication.translate("Driver", u"Back", None))
    # retranslateUi


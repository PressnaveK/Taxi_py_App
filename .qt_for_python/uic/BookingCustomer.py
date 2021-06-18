# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BookingCustomer.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_BookingCustomer(object):
    def setupUi(self, BookingCustomer):
        if not BookingCustomer.objectName():
            BookingCustomer.setObjectName(u"BookingCustomer")
        BookingCustomer.resize(1054, 699)
        BookingCustomer.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.vb_widget = QTableWidget(BookingCustomer)
        if (self.vb_widget.columnCount() < 13):
            self.vb_widget.setColumnCount(13)
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
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font);
        self.vb_widget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.vb_widget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font);
        self.vb_widget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font);
        self.vb_widget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font);
        self.vb_widget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font);
        self.vb_widget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        self.vb_widget.setObjectName(u"vb_widget")
        self.vb_widget.setGeometry(QRect(140, 110, 771, 521))
        self.vb_widget.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(0, 0, 0);\n"
"border-color: rgb(11, 11, 11);\n"
"background-color: rgb(144, 144, 144);")
        self.label = QLabel(BookingCustomer)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(420, 60, 281, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_back = QPushButton(BookingCustomer)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(820, 50, 80, 25))
        font2 = QFont()
        font2.setPointSize(10)
        self.btn_back.setFont(font2)
        self.btn_back.setStyleSheet(u"background-color: rgb(148, 148, 148);\n"
"color: rgb(0, 0, 0);")

        self.retranslateUi(BookingCustomer)

        QMetaObject.connectSlotsByName(BookingCustomer)
    # setupUi

    def retranslateUi(self, BookingCustomer):
        BookingCustomer.setWindowTitle(QCoreApplication.translate("BookingCustomer", u"Frame", None))
        ___qtablewidgetitem = self.vb_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("BookingCustomer", u"Booking_ID", None));
        ___qtablewidgetitem1 = self.vb_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("BookingCustomer", u"Booking_Status", None));
        ___qtablewidgetitem2 = self.vb_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("BookingCustomer", u"Customer_Name", None));
        ___qtablewidgetitem3 = self.vb_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("BookingCustomer", u"Price", None));
        ___qtablewidgetitem4 = self.vb_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("BookingCustomer", u"Payment Status", None));
        ___qtablewidgetitem5 = self.vb_widget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("BookingCustomer", u"Pickup Address", None));
        ___qtablewidgetitem6 = self.vb_widget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("BookingCustomer", u"Destination Address", None));
        ___qtablewidgetitem7 = self.vb_widget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("BookingCustomer", u"Pickup Date", None));
        ___qtablewidgetitem8 = self.vb_widget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("BookingCustomer", u"Pickup Time", None));
        ___qtablewidgetitem9 = self.vb_widget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("BookingCustomer", u"No. of Passengers", None));
        ___qtablewidgetitem10 = self.vb_widget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("BookingCustomer", u"Booking Date", None));
        ___qtablewidgetitem11 = self.vb_widget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("BookingCustomer", u"FeedBack", None));
        ___qtablewidgetitem12 = self.vb_widget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("BookingCustomer", u"Driver name", None));
        self.label.setText(QCoreApplication.translate("BookingCustomer", u"Booking Info", None))
        self.btn_back.setText(QCoreApplication.translate("BookingCustomer", u"Back", None))
    # retranslateUi


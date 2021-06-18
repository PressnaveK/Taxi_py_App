import os
from pathlib import Path
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
#Ui imports
from Welcome_Ui import Ui_Welcome
from Login_Ui import Ui_Login
from Register_Ui import Ui_Register
from Admin_Inf_Ui import Ui_Admin_Inf
from Customer_Inf_Ui import Ui_Customer_Inf
from Driver_Inf_Ui import Ui_Driver_Inf
from BookingAdmin_Ui import Ui_BookingAdmin
from BookingCustomer_Ui import Ui_BookingCustomer
from BookingDriver_Ui import Ui_BookingDriver
from DriverBooking_Ui import Ui_DriverBooking
from RegisterDriver_Ui import Ui_RegisterDriver
from Driver_Ui import Ui_Driver
from Customer_Ui import Ui_Customer
from Payment_Ui import Ui_Payment
from Confirmation_Ui import Ui_Confirmation



import sqlite3

class Taxi_Application(QMainWindow):
    X = ''
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Welcome()
        self.ui.setupUi(self)
        self.show()
        self.ui.btn_Login.clicked.connect(lambda:self.open_login())
        self.ui.btn_Register.clicked.connect(lambda:self.open_Register())

    def open_login(self):
        self.main = Login_page()
        self.main.show()
        self.hide()
    def open_Register(self):
        self.main = Register_page()
        self.main.show()
        self.hide()

#Class for login UI

class Login_page(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.show()
        self.ui.rAdmin.setChecked(True)
        self.ui.btn_back.clicked.connect(lambda:self.Go_back())
        self.ui.btnlogin_window.clicked.connect(lambda:self.login())

    def Go_back(self):
        self.main = Taxi_Application()
        self.main.show()
        self.hide()
    def Go_Admin_Inf(self):
        self.main = Admin_Inf()
        self.main.show()
        self.hide()
    def Go_Customer_Inf(self):
        self.main = Customer_Inf()
        self.main.show()
        self.hide()
    def Go_Driver_Inf(self):
        self.main = Driver_Inf()
        self.main.show()
        self.hide()
    def login(self):
        if self.ui.txt_User.text() == "" or self.ui.txt_Password.text() == "" :
            self.ui.Warninglbl.setText("Null Entry")
        elif self.ui.rAdmin.isChecked():
            self.admin_login();
        elif self.ui.rCustomer.isChecked():
            self.customer_login();
        else:
            self.driver_login();
    def admin_login(self):
        try:
            conn = sqlite3.connect('TBS.db')
            c = conn.cursor()
            UserNm = self.ui.txt_User.text()
            c.execute('SELECT * FROM Administrator where Username = :User',{'User': UserNm})
            Owner = c.fetchone()
            conn.commit()
            conn.close()
            if self.ui.txt_Password.text() == Owner[1]:
                Taxi_Application.X = self.ui.txt_User.text()
                self.Go_Admin_Inf()
            else:
                self.ui.Warninglbl.setText("Invalid Password")
        except:
            self.ui.Warninglbl.setText("User not found")

    def customer_login(self):
        try:
            conn = sqlite3.connect('TBS.db')
            c = conn.cursor()
            UserNm = self.ui.txt_User.text()
            c.execute('SELECT * FROM Customer where Username = :User',{'User': UserNm})
            Owner = c.fetchone()
            conn.commit()
            conn.close()
            if self.ui.txt_Password.text() == Owner[1]:
                Taxi_Application.X = self.ui.txt_User.text()
                self.Go_Customer_Inf()
            else:
                self.ui.Warninglbl.setText("Invalid Password")
        except:
            self.ui.Warninglbl.setText("User not found")

    def driver_login(self):
        try:
            conn = sqlite3.connect('TBS.db')
            c = conn.cursor()
            UserNm = self.ui.txt_User.text()
            c.execute('SELECT * FROM Driver where Username = :User',{'User': UserNm})
            Owner = c.fetchone()
            conn.commit()
            conn.close()
            if self.ui.txt_Password.text() == Owner[1]:
                Taxi_Application.X = self.ui.txt_User.text()
                self.Go_Driver_Inf()
            else:
                self.ui.Warninglbl.setText("Invalid Password")
        except:
            self.ui.Warninglbl.setText("User not found")

#Class for Register UI
class Register_page(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Register()
        self.ui.setupUi(self)
        self.show()
        self.ui.btn_back.clicked.connect(lambda:self.Go_back())
        self.ui.btn_Register.clicked.connect(lambda:self.Register())
    def Go_back(self):
        self.main = Taxi_Application()
        self.main.show()
        self.hide()
    def Register(self):
        try:
            if self.ui.acc_usernameField.text() =="" or  self.ui.acc_passwordField.text() == "" or self.ui.acc_firstNameField.text() =="" or self.ui.acc_lastNameField.text() == "" or  self.ui.acc_contactNoField.text() == "" or self.ui.acc_emailField.text() == "" or self.ui.acc_addressField.text() == "": 
                self.ui.Warninglbl.setText("Null Entry")
            elif self.ui.acc_passwordField.text() == self.ui.acc_confirmPasswordField.text():
                conn = sqlite3.connect('TBS.db')
                c = conn.cursor()
                Username = self.ui.acc_usernameField.text()
                Password = self.ui.acc_passwordField.text()
                First_Name = self.ui.acc_firstNameField.text()
                Last_Name = self.ui.acc_lastNameField.text() 
                Phone = self.ui.acc_contactNoField.text()
                Email = self.ui.acc_emailField.text()
                Address = self.ui.acc_addressField.text()
                c.execute('INSERT INTO Customer VALUES(?,?,?,?,?,?,?)',(Username,Password,First_Name,Last_Name,Phone,Email,Address) )
                conn.commit()
                conn.close()
                self.main = Login_page()
                self.main.show()
                self.hide()
            else:
                self.ui.Warninglbl.setText("Unmatched Passwords")
        except:
            self.ui.Warninglbl.setText("User Exist")
#User Interface
class Admin_Inf(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Admin_Inf()
        self.ui.setupUi(self)
        self.show()
        self.ui.btnBookingInfo.clicked.connect(lambda:self.Go_bookingInfo())
        self.ui.btnRegDrivers.clicked.connect(lambda:self.Go_RegisterDriver())
        self.ui.btnDriverInfo.clicked.connect(lambda:self.Go_Driver())
        self.ui.btnCustomerInfo.clicked.connect(lambda:self.Go_Customer())
        self.ui.lbl_User.setText(Taxi_Application.X)
    def Go_bookingInfo(self):
        self.main = BookingAdmin_info()
        self.main.show()
        self.hide()
    def Go_RegisterDriver(self):
        self.main = RegisterDriver()
        self.main.show()
        self.hide()
    def Go_Driver(self):
        self.main = Driver()
        self.main.show()
        self.hide()
    def Go_Customer(self):
        self.main = Customer()
        self.main.show()
        self.hide()
#Child Ui Admin_Inf_Ui
class BookingAdmin_info(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_BookingAdmin()
        self.ui.setupUi(self)
        self.show()
        self.ui.btn_back.clicked.connect(lambda:self.Go_back())
        conn = sqlite3.connect('TBS.db')
        c = conn.cursor()
        self.ui.vb_widget.setRowCount(50)
        tablerow = 0
        for column in c.execute('SELECT * FROM Booking Limit 50 '):
            self.ui.vb_widget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(column[0]))
            self.ui.vb_widget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(column[1]))
            self.ui.vb_widget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(column[2]))
            self.ui.vb_widget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(column[3]))
            self.ui.vb_widget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(column[4]))
            self.ui.vb_widget.setItem(tablerow,5,QtWidgets.QTableWidgetItem(column[5]))
            self.ui.vb_widget.setItem(tablerow,6,QtWidgets.QTableWidgetItem(column[6]))
            self.ui.vb_widget.setItem(tablerow,7,QtWidgets.QTableWidgetItem(column[7]))
            self.ui.vb_widget.setItem(tablerow,8,QtWidgets.QTableWidgetItem(column[8]))
            self.ui.vb_widget.setItem(tablerow,9,QtWidgets.QTableWidgetItem(column[9]))
            self.ui.vb_widget.setItem(tablerow,10,QtWidgets.QTableWidgetItem(column[10]))
            self.ui.vb_widget.setItem(tablerow,11,QtWidgets.QTableWidgetItem(column[11]))
            self.ui.vb_widget.setItem(tablerow,12,QtWidgets.QTableWidgetItem(column[12]))
            tablerow += 1
        conn.close()
    def Go_back(self):
        self.main = Admin_Inf()
        self.main.show()
        self.hide()


class RegisterDriver(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_RegisterDriver()
        self.ui.setupUi(self)
        self.show()
        self.ui.btn_back.clicked.connect(lambda:self.Go_back())
    def Go_back(self):
        self.main = Admin_Inf()
        self.main.show()
        self.hide()


class Driver(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Driver()
        self.ui.setupUi(self)
        self.show()
        self.ui.btn_back.clicked.connect(lambda:self.Go_back())
        conn = sqlite3.connect('TBS.db')
        c = conn.cursor()
        self.ui.vb_widget.setRowCount(50)
        tablerow = 0
        for column in c.execute('SELECT * FROM Driver Limit 50 '):
            self.ui.vb_widget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(column[0]))
            self.ui.vb_widget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(column[1]))
            self.ui.vb_widget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(column[2]))
            self.ui.vb_widget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(column[3]))
            self.ui.vb_widget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(column[4]))
            self.ui.vb_widget.setItem(tablerow,5,QtWidgets.QTableWidgetItem(column[5]))
            self.ui.vb_widget.setItem(tablerow,6,QtWidgets.QTableWidgetItem(column[6]))
            tablerow += 1
        conn.close()


    def Go_back(self):
        self.main = Admin_Inf()
        self.main.show()
        self.hide()


class Customer(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Customer()
        self.ui.setupUi(self)
        self.show()
        self.ui.btn_back.clicked.connect(lambda:self.Go_back())
        conn = sqlite3.connect('TBS.db')
        c = conn.cursor()
        self.ui.vb_widget.setRowCount(50)
        tablerow = 0
        for column in c.execute('SELECT * FROM Customer Limit 50 '):
            self.ui.vb_widget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(column[0]))
            self.ui.vb_widget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(column[1]))
            self.ui.vb_widget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(column[2]))
            self.ui.vb_widget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(column[3]))
            self.ui.vb_widget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(column[4]))
            self.ui.vb_widget.setItem(tablerow,5,QtWidgets.QTableWidgetItem(column[5]))
            self.ui.vb_widget.setItem(tablerow,6,QtWidgets.QTableWidgetItem(column[6]))
            tablerow += 1
        conn.close()
    def Go_back(self):
        self.main = Admin_Inf()
        self.main.show()
        self.hide()












class Customer_Inf(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Customer_Inf()
        self.ui.setupUi(self)
        self.show()
        self.ui.btnBookingInfo.clicked.connect(lambda:self.Go_bookingInfo())
        self.ui.btnBook.clicked.connect(lambda:self.Go_DriverBooking())
        self.ui.btnPay.clicked.connect(lambda:self.Go_Payment())
        self.ui.lbl_User.setText(Taxi_Application.X)


    def Go_bookingInfo(self):
        self.main = BookingCustomer_info()
        self.main.show()
        self.hide()
    def Go_DriverBooking(self):
        self.main = DriverBooking()
        self.main.show()
        self.hide()
    def Go_Payment(self):
        self.main = Payment()
        self.main.show()
        self.hide()
#Child Ui Customer_Inf_Ui
class Payment(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui =Ui_Payment()
        self.ui.setupUi(self)
        self.show()
        self.ui.btn_back.clicked.connect(lambda:self.Go_back())
    def Go_back(self):
        self.main = Customer_Inf()
        self.main.show()
        self.hide()

class BookingCustomer_info(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_BookingCustomer()
        self.ui.setupUi(self)
        self.show()
        self.ui.btn_back.clicked.connect(lambda:self.Go_back())
        conn = sqlite3.connect('TBS.db')
        c = conn.cursor()
        self.ui.vb_widget.setRowCount(50)
        tablerow = 0
        for column in c.execute('SELECT * FROM Booking WHERE Customer_Name = :Nm Limit 50 ',{'Nm': Taxi_Application.X}):
            self.ui.vb_widget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(column[0]))
            self.ui.vb_widget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(column[1]))
            self.ui.vb_widget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(column[2]))
            self.ui.vb_widget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(column[3]))
            self.ui.vb_widget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(column[4]))
            self.ui.vb_widget.setItem(tablerow,5,QtWidgets.QTableWidgetItem(column[5]))
            self.ui.vb_widget.setItem(tablerow,6,QtWidgets.QTableWidgetItem(column[6]))
            self.ui.vb_widget.setItem(tablerow,7,QtWidgets.QTableWidgetItem(column[7]))
            self.ui.vb_widget.setItem(tablerow,8,QtWidgets.QTableWidgetItem(column[8]))
            self.ui.vb_widget.setItem(tablerow,9,QtWidgets.QTableWidgetItem(column[9]))
            self.ui.vb_widget.setItem(tablerow,10,QtWidgets.QTableWidgetItem(column[10]))
            self.ui.vb_widget.setItem(tablerow,11,QtWidgets.QTableWidgetItem(column[11]))
            self.ui.vb_widget.setItem(tablerow,12,QtWidgets.QTableWidgetItem(column[12]))
            tablerow += 1
        conn.close()
    def Go_back(self):
        self.main = Customer_Inf()
        self.main.show()
        self.hide()
class DriverBooking(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_DriverBooking()
        self.ui.setupUi(self)
        self.show()
        self.ui.btn_back.clicked.connect(lambda:self.Go_back())
        conn = sqlite3.connect('TBS.db')
        c = conn.cursor()
        for x in c.execute("SELECT Username FROM Driver "):
            self.ui.txt_Driver.addItem(x[0])
        self.ui.btn_book.clicked.connect(lambda:self.booking())


    def Go_back(self):
        self.main = Customer_Inf()
        self.main.show()
        self.hide()
    
















class Driver_Inf(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Driver_Inf()
        self.ui.setupUi(self)
        self.show()
        self.ui.btnBooking_info.clicked.connect(lambda:self.Go_bookingInfo())
        self.ui.btnConfirm .clicked.connect(lambda:self.Go_Confirmation())
        self.ui.lbl_User.setText(Taxi_Application.X)
    def Go_bookingInfo(self):
        self.main = BookingDriver_info()
        self.main.show()
        self.hide()
    def Go_Confirmation(self):
        self.main = Confirmation()
        self.main.show()
        self.hide()

#Child Ui Driver_Inf_Ui
class BookingDriver_info(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_BookingDriver()
        self.ui.setupUi(self)
        self.show()
        conn = sqlite3.connect('TBS.db')
        c = conn.cursor()
        self.ui.vb_widget.setRowCount(50)
        tablerow = 0
        for column in c.execute('SELECT * FROM Booking WHERE Driver_Name = :Nm Limit 50 ',{'Nm': Taxi_Application.X}):
            self.ui.vb_widget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(column[0]))
            self.ui.vb_widget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(column[1]))
            self.ui.vb_widget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(column[2]))
            self.ui.vb_widget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(column[3]))
            self.ui.vb_widget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(column[4]))
            self.ui.vb_widget.setItem(tablerow,5,QtWidgets.QTableWidgetItem(column[5]))
            self.ui.vb_widget.setItem(tablerow,6,QtWidgets.QTableWidgetItem(column[6]))
            self.ui.vb_widget.setItem(tablerow,7,QtWidgets.QTableWidgetItem(column[7]))
            self.ui.vb_widget.setItem(tablerow,8,QtWidgets.QTableWidgetItem(column[8]))
            self.ui.vb_widget.setItem(tablerow,9,QtWidgets.QTableWidgetItem(column[9]))
            self.ui.vb_widget.setItem(tablerow,10,QtWidgets.QTableWidgetItem(column[10]))
            self.ui.vb_widget.setItem(tablerow,11,QtWidgets.QTableWidgetItem(column[11]))
            self.ui.vb_widget.setItem(tablerow,12,QtWidgets.QTableWidgetItem(column[12]))
            tablerow += 1
        conn.close()
        self.ui.btn_back.clicked.connect(lambda:self.Go_back())
    def Go_back(self):
        self.main = Driver_Inf()
        self.main.show()
        self.hide()
class Confirmation(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Confirmation()
        self.ui.setupUi(self)
        self.show()
        self.ui.btn_back.clicked.connect(lambda:self.Go_back())
    def Go_back(self):
        self.main = Driver_Inf()
        self.main.show()
        self.hide()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Taxi_Application()
    sys.exit(app.exec())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Coding\python\Solve-Reconstruction\UI\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1293, 742)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 20, 1181, 51))
        self.widget.setObjectName("widget")
        self.minButton = QtWidgets.QPushButton(self.widget)
        self.minButton.setGeometry(QtCore.QRect(1090, 10, 41, 41))
        self.minButton.setText("")
        self.minButton.setObjectName("minButton")
        self.closeButton = QtWidgets.QPushButton(self.widget)
        self.closeButton.setGeometry(QtCore.QRect(1130, 10, 41, 41))
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.logo = QtWidgets.QLabel(self.widget)
        self.logo.setGeometry(QtCore.QRect(20, 10, 31, 31))
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.id = QtWidgets.QLabel(self.widget)
        self.id.setGeometry(QtCore.QRect(70, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.id.setFont(font)
        self.id.setObjectName("id")
        self.add_btn = QtWidgets.QPushButton(self.widget)
        self.add_btn.setGeometry(QtCore.QRect(990, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")
        self.title = QtWidgets.QLabel(self.widget)
        self.title.setGeometry(QtCore.QRect(530, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.edit_btn = QtWidgets.QPushButton(self.widget)
        self.edit_btn.setGeometry(QtCore.QRect(890, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.edit_btn.setFont(font)
        self.edit_btn.setObjectName("edit_btn")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(50, 70, 211, 651))
        self.widget_2.setObjectName("widget_2")
        self.contents_table = QtWidgets.QTableWidget(self.widget_2)
        self.contents_table.setGeometry(QtCore.QRect(10, 10, 191, 631))
        self.contents_table.setObjectName("contents_table")
        self.contents_table.setColumnCount(0)
        self.contents_table.setRowCount(0)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(260, 70, 971, 651))
        self.widget_3.setObjectName("widget_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.id.setText(_translate("MainWindow", "TextLabel"))
        self.add_btn.setText(_translate("MainWindow", "Add Solve"))
        self.title.setText(_translate("MainWindow", "Solve Reconstruction"))
        self.edit_btn.setText(_translate("MainWindow", "Edit Algs"))

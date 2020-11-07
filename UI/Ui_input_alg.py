# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Coding\python\Solve-Reconstruction\UI\input_alg.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InputWindow(object):
    def setupUi(self, InputWindow):
        InputWindow.setObjectName("InputWindow")
        InputWindow.resize(516, 345)
        self.centralwidget = QtWidgets.QWidget(InputWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 50, 441, 181))
        self.widget.setObjectName("widget")
        self.ok_btn = QtWidgets.QPushButton(self.widget)
        self.ok_btn.setGeometry(QtCore.QRect(170, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ok_btn.setFont(font)
        self.ok_btn.setObjectName("ok_btn")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(10, 10, 441, 41))
        self.widget_3.setObjectName("widget_3")
        self.minButton = QtWidgets.QPushButton(self.widget_3)
        self.minButton.setGeometry(QtCore.QRect(360, 0, 41, 41))
        self.minButton.setText("")
        self.minButton.setObjectName("minButton")
        self.closeButton = QtWidgets.QPushButton(self.widget_3)
        self.closeButton.setGeometry(QtCore.QRect(400, 0, 41, 41))
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        InputWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(InputWindow)
        QtCore.QMetaObject.connectSlotsByName(InputWindow)

    def retranslateUi(self, InputWindow):
        _translate = QtCore.QCoreApplication.translate
        InputWindow.setWindowTitle(_translate("InputWindow", "Input"))
        self.ok_btn.setText(_translate("InputWindow", "OK"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Coding\python\Solve-Reconstruction\UI\warn_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Warn_Dialog(object):
    def setupUi(self, Warn_Dialog):
        Warn_Dialog.setObjectName("Warn_Dialog")
        Warn_Dialog.resize(484, 267)
        self.widget = QtWidgets.QWidget(Warn_Dialog)
        self.widget.setGeometry(QtCore.QRect(50, 70, 361, 151))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(8)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 30, 331, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(120, 100, 111, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.widget_2 = QtWidgets.QWidget(Warn_Dialog)
        self.widget_2.setGeometry(QtCore.QRect(50, 30, 361, 41))
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(150, 6, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Warn_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Warn_Dialog)

    def retranslateUi(self, Warn_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Warn_Dialog.setWindowTitle(_translate("Warn_Dialog", "Dialog"))
        self.pushButton.setText(_translate("Warn_Dialog", "确认"))
        self.label_2.setText(_translate("Warn_Dialog", "WARNING"))

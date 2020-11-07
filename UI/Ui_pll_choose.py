# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Coding\python\Solve-Reconstruction\UI\pll_choose.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PLLWindow(object):
    def setupUi(self, PLLWindow):
        PLLWindow.setObjectName("PLLWindow")
        PLLWindow.resize(771, 701)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        PLLWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(PLLWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 40, 601, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.widget.setFont(font)
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setObjectName("widget")
        self.closeButton = QtWidgets.QPushButton(self.widget)
        self.closeButton.setGeometry(QtCore.QRect(560, 0, 41, 41))
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.minButton = QtWidgets.QPushButton(self.widget)
        self.minButton.setGeometry(QtCore.QRect(520, 0, 41, 41))
        self.minButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minButton.setText("")
        self.minButton.setObjectName("minButton")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(200, 5, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(100, 80, 600, 600))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        PLLWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PLLWindow)
        QtCore.QMetaObject.connectSlotsByName(PLLWindow)

    def retranslateUi(self, PLLWindow):
        _translate = QtCore.QCoreApplication.translate
        PLLWindow.setWindowTitle(_translate("PLLWindow", "PLLWindow"))
        self.label.setText(_translate("PLLWindow", "Choose PLL"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Coding\python\Solve-Reconstruction\UI\oll_choose.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OLLWindow(object):
    def setupUi(self, OLLWindow):
        OLLWindow.setObjectName("OLLWindow")
        OLLWindow.resize(771, 701)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        OLLWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(OLLWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 40, 621, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.widget.setFont(font)
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setObjectName("widget")
        self.closeButton = QtWidgets.QPushButton(self.widget)
        self.closeButton.setGeometry(QtCore.QRect(580, 0, 41, 41))
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.minButton = QtWidgets.QPushButton(self.widget)
        self.minButton.setGeometry(QtCore.QRect(540, 0, 41, 41))
        self.minButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minButton.setText("")
        self.minButton.setObjectName("minButton")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(210, 5, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(100, 80, 621, 600))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        OLLWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(OLLWindow)
        QtCore.QMetaObject.connectSlotsByName(OLLWindow)

    def retranslateUi(self, OLLWindow):
        _translate = QtCore.QCoreApplication.translate
        OLLWindow.setWindowTitle(_translate("OLLWindow", "OLLWindow"))
        self.label.setText(_translate("OLLWindow", "Choose OLL"))

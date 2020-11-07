# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Coding\python\Solve-Reconstruction\UI\add_solve.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddSolveWindow(object):
    def setupUi(self, AddSolveWindow):
        AddSolveWindow.setObjectName("AddSolveWindow")
        AddSolveWindow.resize(771, 701)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        AddSolveWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(AddSolveWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 40, 571, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.widget.setFont(font)
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setObjectName("widget")
        self.closeButton = QtWidgets.QPushButton(self.widget)
        self.closeButton.setGeometry(QtCore.QRect(530, 0, 41, 41))
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.minButton = QtWidgets.QPushButton(self.widget)
        self.minButton.setGeometry(QtCore.QRect(490, 0, 41, 41))
        self.minButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minButton.setText("")
        self.minButton.setObjectName("minButton")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(190, 5, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.add_btn = QtWidgets.QPushButton(self.widget)
        self.add_btn.setGeometry(QtCore.QRect(0, 2, 71, 31))
        self.add_btn.setObjectName("add_btn")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(100, 80, 571, 511))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        AddSolveWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddSolveWindow)
        QtCore.QMetaObject.connectSlotsByName(AddSolveWindow)

    def retranslateUi(self, AddSolveWindow):
        _translate = QtCore.QCoreApplication.translate
        AddSolveWindow.setWindowTitle(_translate("AddSolveWindow", "AddSolveWindow"))
        self.label.setText(_translate("AddSolveWindow", "Add Solve"))
        self.add_btn.setText(_translate("AddSolveWindow", "Add"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(596, 304)
        MainWindow.setFixedSize(596, 304)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl = QtWidgets.QLabel(self.centralwidget)
        self.lbl.setEnabled(True)
        self.lbl.setGeometry(QtCore.QRect(20, 10, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lbl.setFont(font)
        self.lbl.setObjectName("lbl")
        self.enterField = QtWidgets.QLineEdit(self.centralwidget)
        self.enterField.setGeometry(QtCore.QRect(20, 70, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.enterField.setFont(font)
        self.enterField.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.enterField.setMaxLength(8)
        self.enterField.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.enterField.setObjectName("enterField")
        self.c1ent = QtWidgets.QLineEdit(self.centralwidget)
        self.c1ent.setGeometry(QtCore.QRect(50, 220, 31, 31))
        self.c1ent.setObjectName("c1ent")
        self.c1lbl = QtWidgets.QLabel(self.centralwidget)
        self.c1lbl.setEnabled(True)
        self.c1lbl.setGeometry(QtCore.QRect(10, 220, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.c1lbl.setFont(font)
        self.c1lbl.setObjectName("c1lbl")
        self.c2ent = QtWidgets.QLineEdit(self.centralwidget)
        self.c2ent.setGeometry(QtCore.QRect(140, 220, 31, 31))
        self.c2ent.setObjectName("c2ent")
        self.c2lbl = QtWidgets.QLabel(self.centralwidget)
        self.c2lbl.setEnabled(True)
        self.c2lbl.setGeometry(QtCore.QRect(100, 220, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.c2lbl.setFont(font)
        self.c2lbl.setObjectName("c2lbl")
        self.c3ent = QtWidgets.QLineEdit(self.centralwidget)
        self.c3ent.setGeometry(QtCore.QRect(230, 220, 31, 31))
        self.c3ent.setObjectName("c3ent")
        self.c3lbl = QtWidgets.QLabel(self.centralwidget)
        self.c3lbl.setEnabled(True)
        self.c3lbl.setGeometry(QtCore.QRect(190, 220, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.c3lbl.setFont(font)
        self.c3lbl.setObjectName("c3lbl")
        self.c4ent = QtWidgets.QLineEdit(self.centralwidget)
        self.c4ent.setGeometry(QtCore.QRect(320, 220, 31, 31))
        self.c4ent.setObjectName("c4ent")
        self.c4lbl = QtWidgets.QLabel(self.centralwidget)
        self.c4lbl.setEnabled(True)
        self.c4lbl.setGeometry(QtCore.QRect(280, 220, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.c4lbl.setFont(font)
        self.c4lbl.setObjectName("c4lbl")
        self.errorent = QtWidgets.QLineEdit(self.centralwidget)
        self.errorent.setGeometry(QtCore.QRect(410, 220, 31, 31))
        self.errorent.setObjectName("errorent")
        self.errorlbl = QtWidgets.QLabel(self.centralwidget)
        self.errorlbl.setEnabled(True)
        self.errorlbl.setGeometry(QtCore.QRect(370, 220, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.errorlbl.setFont(font)
        self.errorlbl.setObjectName("errorlbl")
        self.errortxt = QtWidgets.QLabel(self.centralwidget)
        self.errortxt.setGeometry(QtCore.QRect(460, 90, 131, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.errortxt.setFont(font)
        self.errortxt.setScaledContents(False)
        self.errortxt.setWordWrap(True)
        self.errortxt.setObjectName("errortxt")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 120, 386, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.p2lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.p2lbl.setFont(font)
        self.p2lbl.setObjectName("p2lbl")
        self.gridLayout.addWidget(self.p2lbl, 0, 1, 1, 1)
        self.p4lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.p4lbl.setFont(font)
        self.p4lbl.setObjectName("p4lbl")
        self.gridLayout.addWidget(self.p4lbl, 0, 6, 1, 1)
        self.p3btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p3btn.setText("")
        self.p3btn.setObjectName("p3btn")
        self.gridLayout.addWidget(self.p3btn, 2, 3, 1, 1)
        self.m1btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.m1btn.setText("")
        self.m1btn.setObjectName("m1btn")
        self.gridLayout.addWidget(self.m1btn, 2, 2, 1, 1)
        self.m4btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.m4btn.setText("")
        self.m4btn.setObjectName("m4btn")
        self.gridLayout.addWidget(self.m4btn, 2, 7, 1, 1)
        self.p1lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.p1lbl.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.p1lbl.setFont(font)
        self.p1lbl.setObjectName("p1lbl")
        self.gridLayout.addWidget(self.p1lbl, 0, 0, 1, 1)
        self.m5lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.m5lbl.setFont(font)
        self.m5lbl.setObjectName("m5lbl")
        self.gridLayout.addWidget(self.m5lbl, 0, 8, 1, 1)
        self.m3lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.m3lbl.setFont(font)
        self.m3lbl.setObjectName("m3lbl")
        self.gridLayout.addWidget(self.m3lbl, 0, 5, 1, 1)
        self.m6btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.m6btn.setText("")
        self.m6btn.setObjectName("m6btn")
        self.gridLayout.addWidget(self.m6btn, 2, 9, 1, 1)
        self.m5btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.m5btn.setText("")
        self.m5btn.setObjectName("m5btn")
        self.gridLayout.addWidget(self.m5btn, 2, 8, 1, 1)
        self.m7btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.m7btn.setText("")
        self.m7btn.setObjectName("m7btn")
        self.gridLayout.addWidget(self.m7btn, 2, 10, 1, 1)
        self.p1btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p1btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p1btn.sizePolicy().hasHeightForWidth())
        self.p1btn.setSizePolicy(sizePolicy)
        self.p1btn.setText("")
        self.p1btn.setObjectName("p1btn")
        self.gridLayout.addWidget(self.p1btn, 2, 0, 1, 1)
        self.p2btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p2btn.setText("")
        self.p2btn.setObjectName("p2btn")
        self.gridLayout.addWidget(self.p2btn, 2, 1, 1, 1)
        self.m7lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.m7lbl.setFont(font)
        self.m7lbl.setObjectName("m7lbl")
        self.gridLayout.addWidget(self.m7lbl, 0, 10, 1, 1)
        self.m3btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.m3btn.setText("")
        self.m3btn.setObjectName("m3btn")
        self.gridLayout.addWidget(self.m3btn, 2, 5, 1, 1)
        self.p4btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p4btn.setText("")
        self.p4btn.setObjectName("p4btn")
        self.gridLayout.addWidget(self.p4btn, 2, 6, 1, 1)
        self.p3lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.p3lbl.setFont(font)
        self.p3lbl.setObjectName("p3lbl")
        self.gridLayout.addWidget(self.p3lbl, 0, 3, 1, 1)
        self.m2btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.m2btn.setText("")
        self.m2btn.setObjectName("m2btn")
        self.gridLayout.addWidget(self.m2btn, 2, 4, 1, 1)
        self.m1lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.m1lbl.setFont(font)
        self.m1lbl.setObjectName("m1lbl")
        self.gridLayout.addWidget(self.m1lbl, 0, 2, 1, 1)
        self.m4lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.m4lbl.setFont(font)
        self.m4lbl.setObjectName("m4lbl")
        self.gridLayout.addWidget(self.m4lbl, 0, 7, 1, 1)
        self.m2lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.m2lbl.setFont(font)
        self.m2lbl.setObjectName("m2lbl")
        self.gridLayout.addWidget(self.m2lbl, 0, 4, 1, 1)
        self.m6lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.m6lbl.setFont(font)
        self.m6lbl.setObjectName("m6lbl")
        self.gridLayout.addWidget(self.m6lbl, 0, 9, 1, 1)
        self.m8lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.m8lbl.setFont(font)
        self.m8lbl.setObjectName("m8lbl")
        self.gridLayout.addWidget(self.m8lbl, 0, 11, 1, 1)
        self.m8btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.m8btn.setText("")
        self.m8btn.setObjectName("m8btn")
        self.gridLayout.addWidget(self.m8btn, 2, 11, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 596, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Метод Хемминга"))
        self.lbl.setText(_translate("MainWindow", "Введите двоичное число длиной от 1 до 8 символов"))
        self.c1lbl.setText(_translate("MainWindow", "c1 = "))
        self.c2lbl.setText(_translate("MainWindow", "c2 = "))
        self.c3lbl.setText(_translate("MainWindow", "c3 = "))
        self.c4lbl.setText(_translate("MainWindow", "c4 = "))
        self.errorlbl.setText(_translate("MainWindow", "Бит"))
        self.errortxt.setText(_translate("MainWindow", "Сделайте одну ошибку"))
        self.p2lbl.setText(_translate("MainWindow", "p2"))
        self.p4lbl.setText(_translate("MainWindow", "p4"))
        self.p1lbl.setText(_translate("MainWindow", "p1"))
        self.m5lbl.setText(_translate("MainWindow", "m5"))
        self.m3lbl.setText(_translate("MainWindow", "m3"))
        self.m7lbl.setText(_translate("MainWindow", "m7"))
        self.p3lbl.setText(_translate("MainWindow", "p3"))
        self.m1lbl.setText(_translate("MainWindow", "m1"))
        self.m4lbl.setText(_translate("MainWindow", "m4"))
        self.m2lbl.setText(_translate("MainWindow", "m2"))
        self.m6lbl.setText(_translate("MainWindow", "m6"))
        self.m8lbl.setText(_translate("MainWindow", "m8"))

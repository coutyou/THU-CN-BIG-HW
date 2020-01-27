# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\CINYOU\Desktop\pys\CN\login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(342, 251)
        self.lineEdit_id = QtWidgets.QLineEdit(login)
        self.lineEdit_id.setGeometry(QtCore.QRect(60, 110, 231, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_id.setFont(font)
        self.lineEdit_id.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.label_id = QtWidgets.QLabel(login)
        self.label_id.setGeometry(QtCore.QRect(110, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_id.setFont(font)
        self.label_id.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id.setObjectName("label_id")
        self.pushButton_login = QtWidgets.QPushButton(login)
        self.pushButton_login.setGeometry(QtCore.QRect(130, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setObjectName("pushButton_login")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Login"))
        self.label_id.setText(_translate("login", "请输入学号："))
        self.pushButton_login.setText(_translate("login", "登录"))

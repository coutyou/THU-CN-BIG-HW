# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\CINYOU\Desktop\pys\CN\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(723, 510)
        self.label_friends = QtWidgets.QLabel(main)
        self.label_friends.setGeometry(QtCore.QRect(60, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_friends.setFont(font)
        self.label_friends.setAlignment(QtCore.Qt.AlignCenter)
        self.label_friends.setObjectName("label_friends")
        self.listWidget_friends = QtWidgets.QListWidget(main)
        self.listWidget_friends.setGeometry(QtCore.QRect(60, 70, 171, 321))
        self.listWidget_friends.setObjectName("listWidget_friends")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_friends.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_friends.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_friends.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_friends.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_friends.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_friends.addItem(item)
        self.textBrowser_msg = QtWidgets.QTextBrowser(main)
        self.textBrowser_msg.setGeometry(QtCore.QRect(310, 70, 341, 221))
        self.textBrowser_msg.setObjectName("textBrowser_msg")
        self.textEdit_input = QtWidgets.QTextEdit(main)
        self.textEdit_input.setGeometry(QtCore.QRect(310, 310, 341, 81))
        self.textEdit_input.setObjectName("textEdit_input")
        self.pushButton_send = QtWidgets.QPushButton(main)
        self.pushButton_send.setGeometry(QtCore.QRect(550, 420, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_send.setFont(font)
        self.pushButton_send.setObjectName("pushButton_send")
        self.pushButton_addFriend = QtWidgets.QPushButton(main)
        self.pushButton_addFriend.setGeometry(QtCore.QRect(90, 450, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_addFriend.setFont(font)
        self.pushButton_addFriend.setObjectName("pushButton_addFriend")
        self.lineEdit_addFriend = QtWidgets.QLineEdit(main)
        self.lineEdit_addFriend.setGeometry(QtCore.QRect(140, 410, 101, 21))
        self.lineEdit_addFriend.setObjectName("lineEdit_addFriend")
        self.label_addFriend = QtWidgets.QLabel(main)
        self.label_addFriend.setGeometry(QtCore.QRect(30, 410, 101, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_addFriend.setFont(font)
        self.label_addFriend.setAlignment(QtCore.Qt.AlignCenter)
        self.label_addFriend.setObjectName("label_addFriend")
        self.pushButton_updateState = QtWidgets.QPushButton(main)
        self.pushButton_updateState.setGeometry(QtCore.QRect(150, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_updateState.setFont(font)
        self.pushButton_updateState.setObjectName("pushButton_updateState")

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Main"))
        self.label_friends.setText(_translate("main", "好友列表"))
        __sortingEnabled = self.listWidget_friends.isSortingEnabled()
        self.listWidget_friends.setSortingEnabled(False)
        item = self.listWidget_friends.item(0)
        item.setText(_translate("main", "2017011626 在线"))
        item = self.listWidget_friends.item(1)
        item.setText(_translate("main", "2017011542 在线"))
        item = self.listWidget_friends.item(2)
        item.setText(_translate("main", "2017011547 在线"))
        item = self.listWidget_friends.item(3)
        item.setText(_translate("main", "3017011626 在线"))
        item = self.listWidget_friends.item(4)
        item.setText(_translate("main", "3017011542 在线"))
        item = self.listWidget_friends.item(5)
        item.setText(_translate("main", "3017011547 在线"))
        self.listWidget_friends.setSortingEnabled(__sortingEnabled)
        self.pushButton_send.setText(_translate("main", "发送"))
        self.pushButton_addFriend.setText(_translate("main", "确认添加"))
        self.label_addFriend.setText(_translate("main", "添加好友："))
        self.pushButton_updateState.setText(_translate("main", "刷新"))

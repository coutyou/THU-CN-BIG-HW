from Ui_main import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ConnectServer import *
from P2P import *
import time

class Window_main(QMainWindow, Ui_main):

    updateSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setSlot()
        self.show()

        self.clients = []

    def setID(self, id):
        self.id = id
        self.port = int(id[-3:]) + 1000
        self.server = Server(self.port, self.id, self.textBrowser_msg)
        self.server.showMsgByIdSignal.connect(self.showMsgById_slot)
        self.server.setOnlineSignal.connect(self.setOnline)
        self.server.setOfflineSignal.connect(self.setOffline)
        self.updateSignal.connect(self.updateState)
        self.delSelfId()

        self.updateState()
        self.updateThread = threading.Thread(target=self.updateWhile)
        self.updateThread.daemon = True
        self.updateThread.start()

    def delSelfId(self):
         for i in range(self.listWidget_friends.count()):
            curItem = self.listWidget_friends.item(i)
            id = curItem.text()[:10]
            if id == self.id:
                self.listWidget_friends.takeItem(self.listWidget_friends.row(curItem))
                break

    def updateState(self):
        for i in range(self.listWidget_friends.count()):
            id = self.listWidget_friends.item(i).text()[:10]
            if ConnectServer.query(id) == 'n':
                state = " 离线"
            else:
                state = " 在线"
            text = id + state
            self.listWidget_friends.item(i).setText(text)

    def updateWhile(self):
        while True:
            self.updateSignal.emit()
            time.sleep(5)

    def setOffline(self, off_id):
        for i in range(self.listWidget_friends.count()):
            id = self.listWidget_friends.item(i).text()[:10]
            if id == off_id:
                text = id + " 离线"
                self.listWidget_friends.item(i).setText(text)
                break

    def setOnline(self, on_id):
        for i in range(self.listWidget_friends.count()):
            id = self.listWidget_friends.item(i).text()[:10]
            if id == on_id:
                text = id + " 在线"
                self.listWidget_friends.item(i).setText(text)
                break

    # 设置槽函数
    def setSlot(self):
        self.pushButton_send.clicked.connect(self.sendPressed)
        self.pushButton_addFriend.clicked.connect(self.addFriend)
        self.listWidget_friends.itemClicked.connect(self.friendsClicked)
        self.pushButton_updateState.clicked.connect(self.updateState)

    def addFriend(self):
        friend_id = self.lineEdit_addFriend.text()
        if not ConnectServer.checkValid(friend_id):
            QMessageBox.warning(self, "Warning", "没有该学号！")
        else:
            self.listWidget_friends.addItem(friend_id)
            self.updateState()

    def showRecord_slot(self):
        c = self.sender()
        c.showRecord()

    def removeClient_slot(self):
        c = self.sender()
        self.clients.remove(c)
        self.setOffline(c.dst_id)

    def showMsgById_slot(self, id):
        s = self.sender()
        s.showMsgById(id)

    def friendsClicked(self, item):
        self.textBrowser_msg.clear()
        self.setCurMsgId(item.text()[:10])
        self.updateState()

    def setCurMsgId(self, id):
        self.server.setCurMsgId(id)
        for c in self.clients:
            c.setCurMsgId(id)

    def sendPressed(self):
        msg = self.textEdit_input.toPlainText()

        if self.textBrowser_msg.toPlainText() == "":
            dst_id = self.server.curMsgId
            dst_ip = ConnectServer.query(dst_id)

            if dst_ip != "n":
                if self.listWidget_friends.selectedItems():
                    dst_port = int(dst_id[-3:]) + 1000
                    newClient = Client(dst_ip, dst_port, dst_id, self.id, self.textBrowser_msg)
                    self.clients.append(newClient)
                    newClient.sendMsg(msg)
                    newClient.showRecordSignal.connect(self.showRecord_slot)
                    newClient.removeClientSignal.connect(self.removeClient_slot)

                    self.friendsClicked(self.listWidget_friends.currentItem())
                else:
                    QMessageBox.warning(self, "Warning", "请选择一个用户！")
            else:
                QMessageBox.warning(self, "Warning", "该用户不在线！")
        else:
            foundId = False
            if self.server.curMsgId in self.server.src_ids:
                self.server.sendMsg(self.server.curMsgId, msg)
                foundId = True
            else:
                for c in self.clients:
                    if c.dst_id == self.server.curMsgId:
                        c.sendMsg(msg)
                        foundId = True
                        break
            
            if not foundId:
                dst_id = self.server.curMsgId
                dst_ip = ConnectServer.query(dst_id)
                if dst_ip != "n":
                    dst_port = int(dst_id[-3:]) + 1000
                    newClient = Client(dst_ip, dst_port, dst_id, self.id, self.textBrowser_msg)
                    self.clients.append(newClient)
                    newClient.sendMsg(msg)
                    newClient.showRecordSignal.connect(self.showRecord_slot)
                    newClient.removeClientSignal.connect(self.removeClient_slot)

                    self.friendsClicked(self.listWidget_friends.currentItem())
                else:
                    QMessageBox.warning(self, "Warning", "该用户不在线！")

        self.textEdit_input.clear()

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self,
                                               "Question",
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            logout = ConnectServer.logout(self.id)
            if DEBUG_MODE:
                if logout:
                    print("Successfully logout --from logout")
                else:
                    print("Fail to logout --from logout")       
        else:
            event.ignore()

from Ui_login import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ConnectServer import *
from Window_main import *

class Window_login(QMainWindow, Ui_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setSlot()
        self.show()
    # 设置槽函数
    def setSlot(self):
        self.pushButton_login.clicked.connect(self.loginPressed)

    def loginPressed(self):
        id = self.lineEdit_id.text()
        if not ConnectServer.checkValid(id):
            QMessageBox.warning(self, "Warning", "没有该学号！")
        else:
            self.m = Window_main()
            self.m.setID(id)
            login = ConnectServer.login(id) 
            if DEBUG_MODE:
                if login:
                    print("Successfully login --from login")
                else:
                    print("Fail to login --from login")
            self.close()
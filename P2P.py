import socket
import threading
import inspect
import ctypes
from ConnectServer import DEBUG_MODE
from PyQt5.QtCore import pyqtSignal, QObject

# def _async_raise(tid, exctype):
#     tid = ctypes.c_long(tid)
#     if not inspect.isclass(exctype):
#         exctype = type(exctype)
#     res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
#     if res == 0:
#         raise ValueError("invalid thread id")
#     elif res != 1:
#         ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
#         raise SystemError("PyThreadState_SetAsyncExc failed")
        
# def stop_thread(thread):
#     _async_raise(thread.ident, SystemExit)

class Server(QObject):

    showMsgByIdSignal = pyqtSignal(str)
    setOfflineSignal = pyqtSignal(str)
    setOnlineSignal = pyqtSignal(str)

    def __init__(self, port, id, textBrowser_msg):
        super().__init__()
        self.connections = []
        self.addresses = []
        self.src_ids = []
        self.id = id
        self.msgRecords = []
        self.textBrowser_msg = textBrowser_msg
        self.curMsgId = ""

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('0.0.0.0', port))
        self.sock.listen(5)

        listenConnectionThread = threading.Thread(target=self.listenConnection)
        listenConnectionThread.daemon = True
        listenConnectionThread.start()
        if DEBUG_MODE:
            print("Server running ...")
        
    def __del__(self):
        for c in self.connections:
            c.close()

    def listenConnection(self):    
        while True:
            c, a = self.sock.accept()
            if DEBUG_MODE:
                print(str(a[0]) + ':' + str(a[1]), "connected")
            listenThread = threading.Thread(target=self.listenMsg, args=(c, a))
            listenThread.daemon = True
            listenThread.start()
            self.connections.append(c)
            self.addresses.append(a)
            self.msgRecords.append("")

    def listenMsg(self, c, a):
        while True:
            try:
                data = c.recv(1024)

                if not data:
                    if DEBUG_MODE: 
                        print(str(a[0]) + ':' + str(a[1]), "disconnectd")
                    idx = self.connections.index(c)
                    self.setOfflineSignal.emit(self.src_ids[idx])
                    self.src_ids.remove(self.src_ids[idx])
                    self.msgRecords.remove(self.msgRecords[idx])
                    self.connections.remove(c)
                    self.addresses.remove(a)
                    c.close()
                    break
                
                data = data.decode("utf-8")
                if data[:10] not in self.src_ids:
                    self.src_ids.append(data[:10])
                    self.setOnlineSignal.emit(data[:10])
                data = data[10:]

                if data != "":
                    idx = self.connections.index(c)
                    if self.msgRecords[idx] != "":
                        self.msgRecords[idx] += "\n"+ self.src_ids[idx] + ":    " + data
                    else:
                        self.msgRecords[idx] += self.src_ids[idx] + ":    " + data

                    if self.src_ids[idx] == self.curMsgId:
                        self.showMsgByIdSignal.emit(self.curMsgId)

            except Exception as e:
                if DEBUG_MODE: 
                    print(e)
                    print(str(a[0]) + ':' + str(a[1]), "disconnectd")
                idx = self.connections.index(c)
                self.setOfflineSignal.emit(self.src_ids[idx])
                self.src_ids.remove(self.src_ids[idx])
                self.msgRecords.remove(self.msgRecords[idx])
                self.connections.remove(c)
                self.addresses.remove(a)
                c.close()
                break

    def sendMsg(self, client_id, msg):
        idx = self.src_ids.index(client_id) if (client_id in self.src_ids) else -1
        
        if self.msgRecords[idx] != "":
            self.msgRecords[idx] += "\n"+ self.id + ":    " + msg
        else:
            self.msgRecords[idx] += self.id + ":    " + msg
        
        c = self.connections[idx]
        c.sendall(msg.encode("utf-8"))

        self.showMsgByIdSignal.emit(client_id)

    def showMsgById(self, client_id):
        idx = self.src_ids.index(client_id) if (client_id in self.src_ids) else -1
        self.textBrowser_msg.setText(self.msgRecords[idx])

    def setCurMsgId(self, id):
        self.curMsgId = id
        if id in self.src_ids:
            self.showMsgByIdSignal.emit(id)

class Client(QObject):

    showRecordSignal = pyqtSignal()
    removeClientSignal = pyqtSignal()

    def __init__(self, dst_ip, dst_port, dst_id, src_id, textBrowser_msg):
        super().__init__()
        self.record = ""
        self.src_id = src_id
        self.dst_id = dst_id
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.textBrowser_msg = textBrowser_msg
        self.curMsgId = ""
        self.toUpdate = False

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.connect((dst_ip, dst_port))

        self.listenThread = threading.Thread(target=self.listenMsg, args=(self.textBrowser_msg, self.record))
        self.listenThread.daemon = True
        self.listenThread.start()

        self.sock.send(self.src_id.encode("utf-8"))
    
    def __del__(self):
        self.sock.close()

    def listenMsg(self, textBrowser_msg, record):
        while True:
            try:
                data = self.sock.recv(1024)

                if not data:
                    self.sock.close()
                    self.removeClientSignal.emit()
                    break

                data = data.decode("utf-8")
                if self.record != "":
                    self.record += "\n"+ self.dst_id + ":    " + data
                else:
                    self.record += self.dst_id + ":    " + data

                if self.dst_id == self.curMsgId:
                    self.showRecordSignal.emit()

            except Exception as e:
                if DEBUG_MODE: 
                    print(e)
                self.removeClientSignal.emit()
                self.sock.close()
                break
            
    
    def sendMsg(self, msg):
        if self.record != "":
            self.record += "\n"+ self.src_id + ":    " + msg
        else:
            self.record += self.src_id + ":    " + msg
        
        msg = self.src_id + msg
        self.sock.sendall(msg.encode("utf-8"))

        self.showRecordSignal.emit()

    def showRecord(self):
        self.textBrowser_msg.setText(self.record)

    def setCurMsgId(self, id):
        self.curMsgId = id
        if id == self.dst_id:
            self.showRecordSignal.emit()

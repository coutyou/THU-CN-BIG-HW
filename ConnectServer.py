# -*- coding: UTF-8 -*-
import socket
import re

IP = '166.111.140.57'
PORT = 8000
PASSWORD = 'net2019'
TESTID = '2017011542'
DEBUG_MODE = True

class ConnectServer(object):

    @staticmethod
    def login(id):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
        data = id + '_' + PASSWORD
        s.sendall(data.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        s.close()
        return data == 'lol'

    @staticmethod
    def query(id):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
        data = 'q' + id
        s.sendall(data.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        s.close()
        return data

    @staticmethod
    def logout(id):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
        data = 'logout' + id
        s.sendall(data.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        s.close()
        return data == 'loo'

    @classmethod
    def checkValid(cls, id):
        regex = re.compile('^(\d{1,3}\.?){4}|n$')
        return len(id) == 10 and regex.match(cls.query(id))

    @classmethod
    def testConnection(cls, id):
        try:
            if cls.login(id) and cls.logout(id):
                if DEBUG_MODE:
                    print("Ok --from testConnection") 
                return True
            else:
                if DEBUG_MODE:
                    print("Error --from testConnection")
                return False
        except Exception as e:
            if DEBUG_MODE:
                print(e,"--from testConnection")
            return False
            
if __name__ == '__main__':
    ConnectServer.testConnection(TESTID)
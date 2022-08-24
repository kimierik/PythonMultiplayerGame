#this file contains a class that has alot of code on the client to server communication
import socket


class client:
    def __init__(self,ip,port,proto):
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ip=ip
        self.port=port
        self.proto=proto
        try:
            self.s.connect((self.ip,self.port))
        except:
            print("ip incorrect or server down")
            quit()

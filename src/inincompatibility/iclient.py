import os
import socket
import pickle

class IClient:
    def __init__(self, addr, buffer_size = 4096):
        self.buffer_size = buffer_size
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect(addr)

    def func_eval(self, func, args, kwargs):
        data = pickle.dumps((func, args, kwargs))
        self.client.sendall(data)
        return pickle.loads(self.client.recv(self.buffer_size))

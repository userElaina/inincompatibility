import sys
import socket
import pickle
import torch
from torch import Tensor

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1', 13587))

BUFFER_SIZE = 4096

def calc(*args, **kwargs):
    data = pickle.dumps(('calc', args, kwargs))
    client.sendall(data)
    return pickle.loads(client.recv(BUFFER_SIZE))


def getdata(*args, **kwargs):
    data = pickle.dumps(('getdata', args, kwargs))
    client.sendall(data)
    return pickle.loads(client.recv(BUFFER_SIZE))

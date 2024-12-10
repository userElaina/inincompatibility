import socket
import pickle

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1', 52271))

BUFFER_SIZE = 4096

def _func_eval(func, args, kwargs):
    data = pickle.dumps((func, args, kwargs))
    client.sendall(data)
    return pickle.loads(client.recv(BUFFER_SIZE))


def calc(*args, **kwargs):
    return _func_eval('calc', args, kwargs)


def getdata(*args, **kwargs):
    return _func_eval('getdata', args, kwargs)

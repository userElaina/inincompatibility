# Generated by `inincompatibility`.
# **Not** depend on `incompatibility`. :)
# You can directly `import` this file in another environment.
import socket
import pickle

BUFFER_SIZE = 65536

client = socket.socket(2, socket.SOCK_STREAM)
client.connect(('server.mil', 23333))


def _func_eval(func, args, kwargs):
    data = pickle.dumps((func, args, kwargs))
    client.sendall(data)
    return pickle.loads(client.recv(BUFFER_SIZE))


def _inincompatibility_remote_eval(*args, **kwargs):
    return _func_eval('_inincompatibility_remote_eval', args, kwargs)


def _inincompatibility_remote_exec(*args, **kwargs):
    return _func_eval('_inincompatibility_remote_exec', args, kwargs)


def llm_qa(*args, **kwargs):
    return _func_eval('llm_qa', args, kwargs)

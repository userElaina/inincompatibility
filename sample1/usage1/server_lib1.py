import socket
import pickle

from lib1 import getdata, calc

BUFFER_SIZE = 4096

mian = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mian.bind(('0.0.0.0', 0))
print(mian.getsockname())
mian.listen(1)

FUNC_NAME = {
    'calc': calc,
    'getdata': getdata
}


def eval_from_data(b: bytes) -> bytes:
    func, args, kwargs = pickle.loads(b)
    assert isinstance(func, str)
    assert isinstance(args, tuple)
    assert isinstance(kwargs, dict)
    assert func in FUNC_NAME
    print(func, args, kwargs)
    res = FUNC_NAME[func](*args, **kwargs)
    return pickle.dumps(res)


while True:
    s, addr = mian.accept()
    print('Connected by', addr)
    while True:
        data = s.recv(BUFFER_SIZE)
        if not data:
            break
        res = eval_from_data(data)
        s.sendall(res)
    s.close()

mian.close()

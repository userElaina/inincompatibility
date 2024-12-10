from inincompatibility import IClient

iicc = IClient(('localhost', 4541))

def calc(*args, **kwargs):
    return iicc.func_eval('calc', args, kwargs)


def getdata(*args, **kwargs):
    return iicc.func_eval('getdata', args, kwargs)

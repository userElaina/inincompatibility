from inincompatibility.iclient import IClient

iicc = IClient(('localhost', 35777))

def calc(*args, **kwargs):
    return iicc.func_eval('calc', args, kwargs)


def getdata(*args, **kwargs):
    return iicc.func_eval('getdata', args, kwargs)

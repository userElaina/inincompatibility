from inincompatibility import IClient

inincc = IClient(('localhost', 57497))


def calc(*args, **kwargs):
    return inincc.func_eval('calc', args, kwargs)


def getdata(*args, **kwargs):
    return inincc.func_eval('getdata', args, kwargs)

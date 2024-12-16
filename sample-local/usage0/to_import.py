from torch import Tensor
from inincompatibility import IClient

inincc = IClient(('localhost', 57043))


def calc(x: Tensor, eta: Tensor) -> Tensor:
    # return inincc.func_eval('calc', args, kwargs)
    return inincc.func_eval('calc', (x, eta), dict())


def getdata(i: int) -> str:
    # return inincc.func_eval('getdata', args, kwargs)
    return inincc.func_eval('getdata', (i,), dict())

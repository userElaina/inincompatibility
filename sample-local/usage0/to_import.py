from torch import Tensor
from inincompatibility import IClient

inincc = IClient(('localhost', 23333))


def _inincompatibility_remote_eval(*args, **kwargs):
    return inincc.func_eval('_inincompatibility_remote_eval', args, kwargs)


def _inincompatibility_remote_exec(*args, **kwargs) -> None:
    inincc.func_eval('_inincompatibility_remote_exec', args, kwargs)


def time_out(t: float) -> tuple:
    return inincc.func_eval('time_out', (t,), dict())

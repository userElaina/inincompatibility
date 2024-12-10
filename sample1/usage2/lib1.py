import torch
from torch import Tensor

assert str(torch.__version__).startswith('2.')

data = ['aaa bbb ccc'] * 100

def calc(x: Tensor, eta: Tensor) -> Tensor:
    return torch.exp(x + eta) / (1 + torch.exp(x + eta))

def getdata(i: int) -> str:
    return data[i]

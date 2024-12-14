import torch
from torch import Tensor
from to_import import getdata, calc

assert str(torch.__version__).startswith('1.')

print(getdata(0))
print(calc(Tensor([1.0, 2.0, 3.0]), Tensor([0.1, 0.2, 0.3])))

# aaa bbb ccc
# tensor([0.7503, 0.9002, 0.9644])

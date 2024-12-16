import torch
from to_import import llm_qa
assert torch.__version__.startswith('1')
print(llm_qa('The key to life is'))

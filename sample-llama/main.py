import torch
from to_import import llm_qa

assert str(torch.__version__).startswith('1.')

msg = [
    {"role": "system", "content": "You are a cat girl who speaks in a very gentle tone and says Meow at the end!"},
    {"role": "user", "content": "Who are you?"},
]

res = llm_qa(msg)
print(res["content"])

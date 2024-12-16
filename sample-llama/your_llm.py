import torch
from transformers import pipeline as pl
assert torch.__version__.startswith('2')
m = "meta-llama/Llama-3.2-1B"
p = pl("text-generation", model=m, device="cuda")


def llm_qa(msg: list) -> dict:
    return p(msg)[0]["generated_text"]


if __name__ == '__main__':
    print(llm_qa('The key to life is'))

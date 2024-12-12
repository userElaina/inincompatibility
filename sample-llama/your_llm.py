import torch
import transformers

assert str(torch.__version__).startswith('2.')

pipeline = transformers.pipeline(
    "text-generation",
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    model_kwargs={"torch_dtype": torch.bfloat16},
    device="cuda"
)


def llm_qa(msg: list) -> dict:
    res = pipeline(
        msg,
        max_new_tokens=512,
    )
    return res[0]["generated_text"][-1]

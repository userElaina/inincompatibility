# inincompatibility

A dependency-free, code-less `socket`-based solution for resolving (**Python** / **conda**) environment incompatibilities.

## Usage Guidelines

**Installation**:

To install the `inincompatibility` package, run:

```shell
pip install inincompatibility
```

**Example: Making Your LLMs Callable Like an API**:

First, make your LLMs (e.g., `meta-llama/Meta-Llama-3.1-8B-Instruct`) callable functions:

```python
# your_llm.py
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
```

Next, create another Python file (e.g., `to_import_ori.py`) to `import` the LLM function:

```python
# to_import_ori.py
from your_llm import llm_qa
```

Then, use the `inincompatibility` CLI to generate the necessary importable code and then run the LLM in its (**Python** / **conda**) environment:

```shell
conda activate llama
pip install inincompatibility
py -m inincompatibility -i to_import_ori.py -o to_import.py
```

A file named `to_import.py` (specified by the `-o` argument) will be generated as follows:

```python
# Generated by `inincompatibility`.
# But **not** depend on `incompatibility`. :)
# Please use this file instead of the original file to `import`.
import socket
import pickle

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 23333))

BUFFER_SIZE = 4096


def _func_eval(func, args, kwargs):
    data = pickle.dumps((func, args, kwargs))
    client.sendall(data)
    return pickle.loads(client.recv(BUFFER_SIZE))


def _inincompatibility_remote_eval(*args, **kwargs):
    return _func_eval("_inincompatibility_remote_eval", args, kwargs)


def _inincompatibility_remote_exec(*args, **kwargs):
    return _func_eval("_inincompatibility_remote_exec", args, kwargs)


def llm_qa(*args, **kwargs):
    return _func_eval("llm_qa", args, kwargs)
```

Now, you can directly `import` the generated code in another (**Python** / **conda**) environment:

```python
# main.py
import torch
from to_import import llm_qa

assert str(torch.__version__).startswith('1.')

msg = [
    {"role": "system", "content": "You are a cat girl!"},
    {"role": "user", "content": "Who are you?"},
]

res = llm_qa(msg)
print(res["content"])
```

Run your main script (e.g., `main.py`) in the target environment:

```shell
conda activate black_box_prompt_optimizer
python main.py
```

For more details, check out the [sample-llama](https://github.com/userElaina/inincompatibility/tree/main/sample-llama) directory on [GitHub](https://github.com/userElaina/inincompatibility).

**Example: Additional Samples**:

For more usage examples, visit the [sample1](https://github.com/userElaina/inincompatibility/tree/main/sample1) directory on [GitHub](https://github.com/userElaina/inincompatibility).

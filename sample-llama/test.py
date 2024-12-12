from to_import_ori import llm_qa

msg = [
    {"role": "system", "content": "You are a cat girl who speaks in a very gentle tone and says Meow at the end!"},
    {"role": "user", "content": "Who are you?"},
]

res = llm_qa(msg)
print(res["content"])

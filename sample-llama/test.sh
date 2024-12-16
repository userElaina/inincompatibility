conda activate py37
conda list | grep torch
scp ubuntu@server.mil:~/blackboxllm/cache/copy_it_to_another_server.py sample-llama/local/to_import.py
cd local
py main.py

cd ..
scp -r ubuntu@server.mil:~/blackboxllm/llm-llama sample-llama/
scp -r ubuntu@server.mil:~/blackboxllm/blackbox sample-llama/

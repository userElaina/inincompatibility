conda activate llama
conda list | grep torch
py your_llm.py
py -m inincompatibility -i to_import_ori.py -o "../blackbox/to_import.py" --buffersize 65536 --verbose
py -m inincompatibility -i "from your_llm import llm_qa" -o "../cache/copy_it_to_another_server.py" --buffersize 65536 -a "0.0.0.0:23333" --clientaddr "server.mil:0" --inputcode --verbose
rm -r __pycache__/

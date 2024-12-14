conda activate py311
conda list | grep torch
python server_lib.py

conda activate py37
conda list | grep torch
python main.py

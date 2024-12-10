conda activate py311
conda list | grep torch
py -m inincompatibility -i to_import_bak.py -o to_import.py

conda activate py37
conda list | grep torch
python main.py

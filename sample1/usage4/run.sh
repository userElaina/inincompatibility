conda activate py311
conda list | grep torch
py -m inincompatibility -i to_import_ori.py -o to_import.py --buffersize 8192 -a "0.0.0.0:0" --verbose

conda activate py37
conda list | grep torch
python main.py

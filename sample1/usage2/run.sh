conda activate py311
conda list | grep torch
py -m inincompatibility -i "from lib1 import getdata, calc, _inincompatibility_client_connect_callback; from lib1 import _inincompatibility_client_close_callback;" -o to_import.py --verbose --inputcode

conda activate py37
conda list | grep torch
python main.py

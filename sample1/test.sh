diff sample1/ori/main.py sample1/usage0/main.py
diff sample1/ori/main.py sample1/usage1/main.py
diff sample1/ori/main.py sample1/usage2/main.py
diff sample1/ori/lib1.py sample1/usage0/lib1.py
diff sample1/ori/lib1.py sample1/usage1/lib1.py
diff sample1/ori/lib1.py sample1/usage2/lib1.py

# console 0
conda activate py311
conda list | grep torch
pip install --upgrade -i https://test.pypi.org/simple/ inincompatibility
cd usage0
py server_lib1.py
cd ../usage1
py server_lib1.py
cd ../usage2
py -m inincompatibility -i "from lib1 import getdata, calc, _inincompatibility_client_connect_callback; from lib1 import _inincompatibility_client_close_callback;" -o to_import.py --inputcode --verbose

# console 1
conda activate py37
conda list | grep torch
pip install --upgrade -i https://test.pypi.org/simple/ inincompatibility
cd ori
py main.py
cd ../usage0
py main.py
cd ../usage1
py main.py
cd ../usage2
py main.py

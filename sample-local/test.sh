diff ori/main.py usage0/main.py
diff ori/main.py usage1/main.py
diff ori/main.py usage2/main.py
diff ori/lib1.py usage0/lib1.py
diff usage0/lib1.py usage1/lib1.py
diff usage0/lib1.py usage2/lib1.py
diff usage0/server_lib1.py usage1/server_lib1.py
diff usage1/to_import.py usage2/to_import.py

# console 0
conda activate py311
conda list | grep torch
pip install --upgrade -i https://test.pypi.org/simple/ inincompatibility
cd usage0
py server_lib1.py
cd ../usage1
py server_lib1.py
cd ../usage2
py -m inincompatibility -i "from lib1 import time_out, _inincompatibility_client_connect_callback; from lib1 import _inincompatibility_client_close_callback;" -o to_import.py -a "localhost:23333" --buffersize 4096 --listenn 0 --inputcode --verbose --noexception

# console 1
conda activate py37
conda list | grep torch
pip install --upgrade -i https://test.pypi.org/simple/ inincompatibility
cd ori
py main.py &; py main.py &; py main.py
cd ../usage0
py main.py &; py main.py &; py main.py
cd ../usage1
py main.py &; py main.py &; py main.py
cd ../usage2
py main.py &; py main.py &; py main.py

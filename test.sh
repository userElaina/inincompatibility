# console 0
conda deactivate
py -m build
twine check dist/*
twine upload --repository testpypi dist/* --verbose

diff sample1/ori/main.py sample1/usage0/main.py
diff sample1/ori/main.py sample1/usage1/main.py
diff sample1/ori/main.py sample1/usage2/main.py
diff sample1/ori/main.py sample1/usage3/main.py
diff sample1/ori/lib1.py sample1/usage0/lib1.py
diff sample1/ori/lib1.py sample1/usage1/lib1.py
diff sample1/ori/lib1.py sample1/usage2/lib1.py
diff sample1/ori/lib1.py sample1/usage3/lib1.py


# console 1
conda activate py311
conda list | grep torch
pip install --upgrade -i https://test.pypi.org/simple/ inincompatibility
cd sample1/usage0
py server_lib1.py
cd ../usage1
py server_lib1.py
cd ../usage2
py -m inincompatibility -i to_import_ori.py -o to_import.py --buffersize 8192 -a "0.0.0.0:0" --verbose
cd ../usage3
py -m inincompatibility -i "from lib1 import getdata, calc, _inincompatibility_client_connect_callback; from lib1 import _inincompatibility_client_close_callback;" -o to_import.py --buffersize 8192 -a "0.0.0.0:0" --verbose --inputcode


# console 2
conda activate py37
conda list | grep torch
pip install --upgrade -i https://test.pypi.org/simple/ inincompatibility
cd sample1/ori
py main.py
cd ../usage0
py main.py
cd ../usage1
py main.py
cd ../usage2
py main.py
cd ../usage3
py main.py


# console 0
conda deactivate
py -m build
twine check dist/*
twine upload dist/* --verbose

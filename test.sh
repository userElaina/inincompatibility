conda create -y -n py311 python=3.11
conda create -y -n py37 python=3.7
conda activate py311
conda install pytorch torchvision torchaudio cpuonly -c pytorch
conda activate py37
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 cpuonly -c pytorch

conda deactivate
conda deactivate
py -m build
twine check dist/*
twine upload --repository testpypi dist/* --verbose

conda activate py311
conda list | grep torch
pip install --upgrade -i https://test.pypi.org/simple/ inincompatibility
cd sample1/usage1
py server_lib1.py
cd ../usage2
py server_lib1.py
cd ../usage3
py server_lib1.py
cd ../usage4
py -m inincompatibility -i to_import_bak.py -o to_import.py

conda activate py37
conda list | grep torch
pip install --upgrade -i https://test.pypi.org/simple/ inincompatibility
cd sample1/ori
py main.py
cd ../usage1
py main.py
cd ../usage2
py main.py
cd ../usage3
py main.py
cd ../usage4
py main.py

conda deactivate
conda deactivate
py -m build
twine check dist/*
twine upload dist/* --verbose

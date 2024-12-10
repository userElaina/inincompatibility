conda create -y -n py311 python=3.11
conda create -y -n py37 python=3.7

conda activate py311
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia

conda activate py37
conda install pytorch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 cpuonly -c pytorch

conda deactivate
conda deactivate
py -m build
twine check dist/*
twine upload --repository testpypi dist/*

conda activate py311
pip install -i https://test.pypi.org/simple/ inincompatibility
py -m inincompatibility

conda activate py37
pip install -i https://test.pypi.org/simple/ inincompatibility
py main.py

conda deactivate
conda deactivate
twine upload dist/*

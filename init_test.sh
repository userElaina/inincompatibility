conda create -y -n py311 python=3.11
conda activate py311
# https://pytorch.org/
# 2024.12.12 (PyTorch Stable 2.5.1)
conda install pytorch torchvision torchaudio cpuonly -c pytorch

conda create -y -n py37 python=3.7
conda activate py37
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 cpuonly -c pytorch

conda create -y -n llama python=3.12
conda activate llama
# https://pytorch.org/
# 2024.12.12 (PyTorch Stable 2.5.1)
conda install pytorch torchvision torchaudio transformers pytorch-cuda=12.1 -c pytorch -c nvidia
py test.py
pip install inincompatibility
py -m inincompatibility -i to_import_ori.py -o to_import.py --buffersize 65536 -a "0.0.0.0:0" --verbose

conda create -y -n black_box_prompt_optimizer python=3.7
conda activate black_box_prompt_optimizer
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 cpuonly -c pytorch
py main.py

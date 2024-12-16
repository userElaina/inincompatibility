conda create -y -n llama python=3.12
conda activate llama
# https://pytorch.org/
# 2024.12.12 (PyTorch Stable 2.5.1)
conda install pytorch torchvision torchaudio transformers pytorch-cuda=12.1 -c pytorch -c nvidia
pip install inincompatibility
huggingface-cli login
# hf_AccessToken_CreateNewToken_RepositoriesPermissions

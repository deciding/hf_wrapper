import os
from huggingface_hub import snapshot_download

def hf_download(repo_id, local_dir=None, local_dir_use_symlinks=False):
    if local_dir is None:
        download_dir = 'download'
        os.makedirs(download_dir, exist_ok=True)
        local_dir = os.path.join(download_dir, os.path.basename(repo_id))
    snapshot_download(repo_id, local_dir=local_dir, local_dir_use_symlinks=local_dir_use_symlinks)

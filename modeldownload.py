from huggingface_hub import snapshot_download

# Replace "LanguageBind/Open-Sora-Plan-v1.3.0" with the actual repository name
repo_id = "LanguageBind/Open-Sora-Plan-v1.3.0"
local_dir = "./open_sora_plan_v1_3_0"  # Directory where the repo will be downloaded

# Download the entire repository
snapshot_download(repo_id, local_dir=local_dir)

print(f"Repository downloaded to {local_dir}")

from transformers import MT5ForConditionalGeneration, MT5Tokenizer

# Define the model repository
repo_name = "google/mt5-xxl"

# Specify the local directory to save the model
local_dir = "./mt5-xxl-pytorch"

# Download tokenizer and model files
print("Downloading tokenizer...")
tokenizer = MT5Tokenizer.from_pretrained(repo_name, cache_dir=local_dir)

print("Downloading PyTorch model...")
model = MT5ForConditionalGeneration.from_pretrained(repo_name, cache_dir=local_dir)

print(f"Model and tokenizer downloaded to {local_dir}")

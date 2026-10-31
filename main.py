import kagglehub

# Download latest version
path = kagglehub.dataset_download("olistbr/brazilian-ecommerce", output_dir="./data/raw", force_download=True)

print("Path to dataset files:", path)
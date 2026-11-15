import kagglehub

# Download latest version
path = kagglehub.dataset_download("olistbr/brazilian-ecommerce", output_dir="./data/raw/olist", force_download=True)

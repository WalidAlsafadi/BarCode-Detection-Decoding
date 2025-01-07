import kagglehub

def download_dataset():
    """
    Attempts to download the Barcode and QR dataset using KaggleHub.
    Provides instructions for manual download if the automatic method fails.
    """
    print("Attempting to download the dataset...")
    try:
        # Download the dataset
        path = kagglehub.dataset_download("jonathanimmanuel/barcode-and-qr")
        print("Dataset downloaded successfully!")
        print(f"Path to dataset files: {path}")
    except Exception as e:
        # Handle download errors
        print("========================================")
        print("ERROR: Automatic download failed.")
        print(f"Details: {e}")
        print("\nTo download the dataset manually:")
        print("1. Visit: https://www.kaggle.com/datasets/jonathanimmanuel/barcode-and-qr")
        print("2. Click the 'Download' button.")
        print("3. Extract the dataset and place it in the 'data/raw/' directory.")
        print("========================================")

if __name__ == "__main__":
    download_dataset()
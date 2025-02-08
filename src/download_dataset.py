import kagglehub
import os

def download_dataset():
    """
    Downloads the Barcode and QR dataset using KaggleHub.
    If the automatic download fails, it provides clear instructions for manual download.
    """
    print("[INFO] Attempting to download the dataset...")
    try:
        # Attempt to download the dataset
        path = kagglehub.dataset_download("jonathanimmanuel/barcode-and-qr")
        if os.path.exists(path):
            print("[SUCCESS] Dataset downloaded successfully!")
            print(f"[INFO] Path to dataset files: {path}")
        else:
            raise FileNotFoundError("Downloaded path does not exist.")
    except Exception as e:
        # Handle errors and provide manual download instructions
        print("========================================")
        print("[ERROR] Automatic download failed.")
        print(f"[DETAILS] {e}")
        print("\n[INSTRUCTIONS] To download the dataset manually:")
        print("1. Visit: https://www.kaggle.com/datasets/jonathanimmanuel/barcode-and-qr")
        print("2. Click the 'Download' button.")
        print("3. Extract the dataset and place it in the 'data/raw/' directory.")
        print("========================================")


if __name__ == "__main__":
    download_dataset()
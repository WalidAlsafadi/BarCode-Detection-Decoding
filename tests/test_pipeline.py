import os
import shutil

# Add the project root to the Python path for imports
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from run_pipeline import process_images

# Define paths
INPUT_DIR = "data/raw"
DEBUG_DIR = "tests/test_images/"

def test_pipeline():
    """
    Test the full barcode detection pipeline.
    Ensures processed images are saved in the debug directory for verification.
    """
    # Ensure the debug directory exists
    os.makedirs(DEBUG_DIR, exist_ok=True)

    # Run the pipeline
    process_images()

    # Move processed files to the debug directory
    processed_files = [
        f for f in os.listdir("data/processed") if f.endswith("_detected.jpg")
    ]
    for file in processed_files:
        source_path = os.path.join("data/processed", file)
        target_path = os.path.join(DEBUG_DIR, file)
        shutil.move(source_path, target_path)

    # Assert at least one file was processed and moved
    assert len(processed_files) > 0, "[ERROR] Pipeline did not process any images!"

    # Log results for debugging
    print("[SUCCESS] Pipeline processed the following images:")
    for file in processed_files:
        print(f" - {file}")
    print(f"[INFO] Processed images moved to: {DEBUG_DIR}")

if __name__ == "__main__":
    test_pipeline()
    print("[TEST] Full pipeline test completed successfully!")
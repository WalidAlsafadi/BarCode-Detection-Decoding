import os
import pytest
from src.run_pipeline import process_images

# Define input/output directories
INPUT_DIR = "data/raw"
OUTPUT_DIR = "data/processed"
DEBUG_DIR = "tests/test_images/"

def test_pipeline():
    """
    Test the full barcode detection pipeline.
    """
    process_images(INPUT_DIR, OUTPUT_DIR)

    # Ensure at least one processed file exists
    processed_files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith("_detected.jpg")]
    assert len(processed_files) > 0, "Pipeline did not process any images!"

if __name__ == "__main__":
    pytest.main()
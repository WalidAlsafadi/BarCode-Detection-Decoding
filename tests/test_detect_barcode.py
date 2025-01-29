import cv2
import os
import pytest
from src.detect_barcode import detect_barcode

# Define test paths
TEST_IMAGE_PATH = "data/raw/sample_barcode.jpg"
DEBUG_DIR = "tests/test_images/"
DEBUG_DETECTED_PATH = os.path.join(DEBUG_DIR, "debug_detected.jpg")

# Ensure debug directory exists
os.makedirs(DEBUG_DIR, exist_ok=True)

def test_detect_barcode():
    """
    Test barcode detection function.
    """
    detected_image, barcode_regions = detect_barcode(TEST_IMAGE_PATH)

    assert detected_image is not None, "Detection failed: No output image!"
    assert barcode_regions is not None and len(barcode_regions) > 0, "No barcode regions found!"

    # Save debug detected barcode image
    cv2.imwrite(DEBUG_DETECTED_PATH, detected_image)
    assert os.path.exists(DEBUG_DETECTED_PATH), "Debug detected barcode image was not saved!"

if __name__ == "__main__":
    pytest.main()
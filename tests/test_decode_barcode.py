import cv2
import os
import pytest
from src.decode_barcode import decode_barcode

# Define test paths
TEST_IMAGE_PATH = "data/raw/sample_barcode.jpg"
DEBUG_DIR = "tests/test_images/"
DEBUG_DECODED_PATH = os.path.join(DEBUG_DIR, "debug_decoded.jpg")

def test_decode_barcode():
    """
    Test barcode decoding function.
    """
    image = cv2.imread(TEST_IMAGE_PATH)
    decoded_info = decode_barcode(image)

    assert decoded_info is not None, "Decoding failed: No barcodes detected!"
    assert len(decoded_info) > 0, "No barcodes were decoded!"

    # Save debug decoded image
    cv2.imwrite(DEBUG_DECODED_PATH, image)
    assert os.path.exists(DEBUG_DECODED_PATH), "Debug decoded barcode image was not saved!"

if __name__ == "__main__":
    pytest.main()
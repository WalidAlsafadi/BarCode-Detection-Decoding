import os
import cv2

# Add project root for imports
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.decode_barcode import decode_barcode

# Constants for test paths
TEST_IMAGE_PATH = os.path.join("data", "raw", "05102009108.jpg")

def test_decode_barcode():
    """
    Test the barcode decoding function.
    Ensures barcodes are decoded correctly and outputs the results.
    """
    # Load the test image
    image = cv2.imread(TEST_IMAGE_PATH)
    assert image is not None, f"[ERROR] Failed to load image: {TEST_IMAGE_PATH}"

    # Perform barcode decoding
    decoded_info = decode_barcode(image)

    # Assertions to verify results
    assert decoded_info is not None, "[ERROR] Decoding failed: No barcodes detected!"
    assert len(decoded_info) > 0, "[ERROR] No barcodes were decoded!"

    # Log decoded barcode data
    print("[SUCCESS] Barcode decoding test completed successfully!")
    print("[INFO] Decoded barcodes:")
    for barcode_type, barcode_data in decoded_info:
        print(f"[DECODED] {barcode_type} barcode: {barcode_data}")

if __name__ == "__main__":
    test_decode_barcode()
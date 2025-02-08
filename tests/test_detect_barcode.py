import os
import cv2

# Add the project root to the Python path for imports
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.detect_barcode import detect_barcode

# Constants for test paths
TEST_IMAGE_PATH = os.path.join("data", "raw", "05102009081.jpg")
DEBUG_DIR = os.path.join("tests", "test_images")
DEBUG_DETECTED_PATH = os.path.join(DEBUG_DIR, "debug_detected.jpg")

# Ensure debug directory exists
os.makedirs(DEBUG_DIR, exist_ok=True)

def test_detect_barcode():
    """
    Test the barcode detection function.
    Ensures barcodes are detected and the results are saved correctly.
    """
    # Perform barcode detection
    detected_image, barcode_regions = detect_barcode(TEST_IMAGE_PATH)

    # Assertions to verify results
    assert detected_image is not None, "[ERROR] Detection failed: No output image!"
    assert barcode_regions is not None and len(barcode_regions) > 0, "[ERROR] No barcode regions found!"

    # Save the debug-detected barcode image
    cv2.imwrite(DEBUG_DETECTED_PATH, detected_image)
    assert os.path.exists(DEBUG_DETECTED_PATH), "[ERROR] Debug detected barcode image was not saved!"

    print("[SUCCESS] Barcode detection test completed successfully!")
    print(f"[INFO] Debug detected image saved at: {DEBUG_DETECTED_PATH}")

if __name__ == "__main__":
    test_detect_barcode()
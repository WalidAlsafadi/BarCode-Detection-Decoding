import os
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from detect_barcode import detect_barcode_contours

def test_detect_barcode():
    """
    Test the detect_barcode_contours function.
    """
    # Paths for input and output
    processed_image_path = "data/processed/05102009083_processed.jpg"
    original_image_path = "data/raw/05102009083.jpg"
    detected_image_path = "data/processed/05102009083_detected.jpg"

    # Check if the required input files exist
    if not os.path.exists(processed_image_path):
        print(f"Processed image not found: {processed_image_path}")
        return
    if not os.path.exists(original_image_path):
        print(f"Original image not found: {original_image_path}")
        return

    # Run the barcode detection function
    print("Running barcode detection...")
    barcode_contour = detect_barcode_contours(processed_image_path, original_image_path)

    # Verify results
    if barcode_contour is None:
        print("No barcode detected in the image.")
    else:
        print(f"Barcode detected successfully. Output saved at: {detected_image_path}")

if __name__ == "__main__":
    test_detect_barcode()
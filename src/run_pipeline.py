import os
import sys
import cv2

# Ensure the src directory is recognized as a module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.detect_barcode import detect_barcode
from src.decode_barcode import decode_barcode

# Directories
INPUT_DIR = "data/raw"
OUTPUT_DIR = "data/processed"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def process_single_image(image_path):
    """
    Processes a single image: detects barcode and decodes it.
    """
    print(f"[INFO] Processing image: {image_path}")

    # Step 1: Detect Barcode
    detected_image, barcode_regions = detect_barcode(image_path)

    if detected_image is not None and len(barcode_regions) > 0:
        print("[SUCCESS] Barcode detected.")

        # Step 2: Decode the barcode(s)
        decoded_info = []
        for barcode_region in barcode_regions:
            decoded_info.extend(decode_barcode(barcode_region))

        # Step 3: Save processed image
        output_path = os.path.join(OUTPUT_DIR, "sample_barcode_detected.jpg")
        cv2.imwrite(output_path, detected_image)
        print(f"[INFO] Processed image saved at: {output_path}")

        # Step 4: Print decoded info
        if decoded_info:
            for barcode_type, barcode_data in decoded_info:
                print(f"[DECODED] {barcode_type} barcode: {barcode_data}")
        else:
            print("[WARNING] Barcode detected, but decoding failed.")
    else:
        print("[ERROR] No barcode detected.")

def process_images():
    """
    Processes all images in the input directory.
    """
    print("[INFO] Processing all images in the dataset...")
    
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            input_path = os.path.join(INPUT_DIR, filename)
            process_single_image(input_path)

if __name__ == "__main__":
    process_single_image("data/raw/05102009140.jpg")  # Testing with one image for now
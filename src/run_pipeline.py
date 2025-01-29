import os
import cv2
from src.detect_barcode import detect_barcode
from src.decode_barcode import decode_barcode

# Change this to process only one image for now
TEST_IMAGE_PATH = "data/raw/sample_barcode.jpg"
OUTPUT_DIR = "data/processed"

def process_single_image(image_path):
    """
    Processes a single image: detects barcode and decodes it.
    """
    print(f"[INFO] Processing image: {image_path}")

    # Step 1: Detect Barcode
    detected_image, barcode_regions = detect_barcode(image_path)

    if detected_image is not None and barcode_regions:
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

if __name__ == "__main__":
    process_single_image(TEST_IMAGE_PATH)
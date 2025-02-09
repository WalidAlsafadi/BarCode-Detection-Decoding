import os
import cv2
from src.detect_barcode import detect_barcode
from src.decode_barcode import decode_barcode

# Define input and output directories
INPUT_DIR = "data/raw"
OUTPUT_DIR = "data/processed"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def process_single_image(image_path):
    """
    Processes a single image: detects barcode and decodes it.
    """
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    print(f"[INFO] Processing image: {image_name}")

    # Detect Barcode
    detected_image, barcode_regions = detect_barcode(image_path)

    if detected_image is not None and barcode_regions is not None and len(barcode_regions) > 0:
        print(f"[SUCCESS] Barcode detected in {image_name}.")

        # Decode the barcode(s)
        decoded_info = set()  # Use a set to avoid duplicate barcode data
        for barcode_region in barcode_regions:
            if barcode_region is not None and barcode_region.size > 0:  # Filter valid regions
                barcodes = decode_barcode(barcode_region)
                if barcodes:  # Only add non-empty results
                    decoded_info.update(barcodes)

        # Save processed image with proper naming
        output_path = os.path.join(OUTPUT_DIR, f"{image_name}_detected.jpg")
        cv2.imwrite(output_path, detected_image)
        print(f"[INFO] Processed image saved at: {output_path}")

        # Print decoded info
        if decoded_info:
            for barcode_type, barcode_data in decoded_info:
                print(f"[DECODED] {barcode_type} barcode: {barcode_data}")
        else:
            print(f"[WARNING] Barcode detected in {image_name}, but decoding failed.")
    else:
        print(f"[ERROR] No barcode detected in {image_name}.")

def process_images():
    """
    Processes all images in the input directory.
    Saves each processed image with a proper naming convention.
    """
    print("[INFO] Processing all images in the dataset...")
    images_found = False

    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            images_found = True
            input_path = os.path.join(INPUT_DIR, filename)
            process_single_image(input_path)

    if not images_found:
        print("[WARNING] No valid image files found in the input directory.")

if __name__ == "__main__":
    try:
        # For testing, process a single image first
        test_image = os.path.join(INPUT_DIR, "05102009170.jpg")
        if os.path.exists(test_image):
            process_single_image(test_image)
        else:
            print(f"[ERROR] Test image not found at {test_image}")

        # Uncomment below to process all images
        #process_images()
    except Exception as e:
        print(f"[CRITICAL ERROR] An unexpected error occurred: {e}")
import os
import cv2

# Add the project root to the Python path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.preprocess import preprocess_image  # Standard import from the src module

# Define test paths
TEST_IMAGE_PATH = os.path.join("data/raw/05102009122.jpg")
DEBUG_DIR = os.path.join("tests/test_images/")
DEBUG_PROCESSED_PATH = os.path.join(DEBUG_DIR, "debug_preprocessed.jpg")

def test_preprocess_image():
    """
    Test the image preprocessing function.
    Ensures the function processes the image correctly and saves the result.
    """
    # Ensure debug directory exists
    os.makedirs(DEBUG_DIR, exist_ok=True)

    # Call preprocess_image and validate output
    processed_image = preprocess_image(TEST_IMAGE_PATH)
    assert processed_image is not None, "[ERROR] Preprocessed image is None!"
    assert processed_image.size > 0, "[ERROR] Preprocessed image is empty!"

    # Save debug preprocessed image
    cv2.imwrite(DEBUG_PROCESSED_PATH, processed_image)
    assert os.path.exists(DEBUG_PROCESSED_PATH), "[ERROR] Debug preprocessed image was not saved!"

    print("[SUCCESS] Preprocessing test completed successfully!")
    print(f"[INFO] Debug preprocessed image saved at: {DEBUG_PROCESSED_PATH}")

if __name__ == "__main__":
    test_preprocess_image()
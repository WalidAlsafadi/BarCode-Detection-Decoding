import cv2
import os
import sys
import pytest

# Ensure the src directory is recognized as a module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.preprocess import preprocess_image

# Define test paths
TEST_IMAGE_PATH = "data/raw/05102009140.jpg"
DEBUG_DIR = "tests/test_images/"
DEBUG_PROCESSED_PATH = os.path.join(DEBUG_DIR, "debug_preprocessed1.jpg")

def test_preprocess_image():
    """
    Test the image preprocessing function.
    """
    processed_image = preprocess_image(TEST_IMAGE_PATH)
    
    assert processed_image is not None, "Preprocessed image is None!"
    assert processed_image.size > 0, "Preprocessed image is empty!"

    # Save debug image
    cv2.imwrite(DEBUG_PROCESSED_PATH, processed_image)
    assert os.path.exists(DEBUG_PROCESSED_PATH), "Debug preprocessed image was not saved!"

if __name__ == "__main__":
    pytest.main()
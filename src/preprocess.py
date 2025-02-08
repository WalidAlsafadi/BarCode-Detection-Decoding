import cv2
import numpy as np

def preprocess_image(image_path):
    """
    Preprocess the image to enhance barcode detection.
    Steps:
    1. Load the image and convert it to grayscale.
    2. Compute gradients to highlight vertical structures.
    3. Apply Gaussian blur and binary thresholding.
    4. Perform morphological operations to close gaps in the barcode.
    5. Remove noise through erosion and dilation.

    Args:
        image_path (str): Path to the image file.

    Returns:
        numpy.ndarray: Preprocessed binary image or None if the image cannot be loaded.
    """
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"[ERROR] Could not load image: {image_path}")
        return None

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Compute gradients in the x-direction
    gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradX = cv2.convertScaleAbs(gradX)

    # Apply Gaussian blur and binary threshold
    blurred = cv2.GaussianBlur(gradX, (5, 5), 0)
    _, binary = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

    # Perform morphological transformations to close gaps
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (27, 7))
    closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

    # Remove noise using erosion and dilation
    closed = cv2.erode(closed, None, iterations=4)
    closed = cv2.dilate(closed, None, iterations=4)

    return closed
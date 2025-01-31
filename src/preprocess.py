import cv2
import numpy as np

def preprocess_image(image_path):
    """
    Preprocess the image to enhance barcode detection.
    - Convert to grayscale
    - Compute gradients
    - Apply thresholding and morphological operations
    """
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image {image_path}")
        return None

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Compute the gradient in the x-direction
    gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradX = cv2.convertScaleAbs(gradX)

    # Blur and apply binary threshold
    blurred = cv2.GaussianBlur(gradX, (6, 6), 0)
    _, binary = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

    # Morphological transformations to close gaps
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
    closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

    # Remove small blobs and noise
    closed = cv2.erode(closed, None, iterations=4)
    closed = cv2.dilate(closed, None, iterations=4)

    return closed
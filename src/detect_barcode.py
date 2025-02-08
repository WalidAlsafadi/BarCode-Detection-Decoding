import cv2
import numpy as np
from src.preprocess import preprocess_image

def detect_barcode(image_path):
    """
    Detects the barcode in the given image and draws a bounding box around it.

    Args:
        image_path (str): Path to the input image.

    Returns:
        tuple: The image with a drawn bounding box (numpy.ndarray) and the cropped barcode region (numpy.ndarray).
    """
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"[ERROR] Could not load image: {image_path}")
        return None, None

    # Preprocess the image to prepare it for contour detection
    processed_image = preprocess_image(image_path)
    if processed_image is None:
        return None, None

    # Find contours
    contours, _ = cv2.findContours(processed_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Sort contours by area and take the largest one
        largest_contour = max(contours, key=cv2.contourArea)

        # Get the rotated bounding box
        rect = cv2.minAreaRect(largest_contour)
        box = cv2.boxPoints(rect)
        box = np.intp(box)  # Convert to integer

        # Draw the rotated bounding box on the original image
        cv2.drawContours(image, [box], -1, (0, 255, 0), 2)

        # Crop the barcode region (using the bounding rectangle)
        x, y, w, h = cv2.boundingRect(largest_contour)
        barcode_region = image[y:y + h, x:x + w]

        return image, barcode_region
    else:
        print("[WARNING] No barcode detected.")
        return None, None
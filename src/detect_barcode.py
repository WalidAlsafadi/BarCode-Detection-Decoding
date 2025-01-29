import cv2
import numpy as np
from src.preprocess import preprocess_image

def detect_barcode(image_path):
    """
    Detects the barcode in the given image and draws a bounding box around it.
    """
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image {image_path}")
        return None

    processed_image = preprocess_image(image_path)
    if processed_image is None:
        return None

    # Find contours
    contours, _ = cv2.findContours(processed_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Sort contours by area and take the largest one
        largest_contour = max(contours, key=cv2.contourArea)
        rect = cv2.minAreaRect(largest_contour)  # Get rotated bounding box
        box = cv2.boxPoints(rect)
        box = np.intp(box)

        # Draw rotated bounding box
        cv2.drawContours(image, [box], -1, (0, 255, 0), 2)

        # Crop the barcode region (rotated bounding box handling will be added later)
        x, y, w, h = cv2.boundingRect(largest_contour)
        barcode_region = image[y:y+h, x:x+w]

        return image, barcode_region
    else:
        print("No barcode detected.")
        return None, None
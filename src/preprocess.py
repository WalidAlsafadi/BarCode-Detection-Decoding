import cv2

def preprocess_image(image_path):
    """
    Preprocess the input image with improved contrast and morphological operations.
    """
    print(f"Loading image: {image_path}")
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load image: {image_path}")
        return None
    else:
        print(f"Image loaded successfully: {image_path}")

    # Convert to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to enhance contrast
    binary = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    # Apply morphological closing with a larger kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 6))
    closed_image = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

    # Apply dilation to merge nearby contours
    dilated_image = cv2.dilate(closed_image, kernel, iterations=2)

    # Save debug images
    cv2.imwrite("data/processed/debug_adaptive_threshold.jpg", binary)
    cv2.imwrite("data/processed/debug_morph_closing.jpg", closed_image)
    cv2.imwrite("data/processed/debug_dilated.jpg", dilated_image)

    return dilated_image
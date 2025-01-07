import cv2

def detect_barcode_contours(processed_image_path, original_image_path):
    """
    Detect the barcode region in the processed image using contours and highlight it on the original image.
    """
    # Load the processed and original images
    processed_image = cv2.imread(processed_image_path, cv2.IMREAD_GRAYSCALE)
    original_image = cv2.imread(original_image_path)

    # Find contours
    contours, _ = cv2.findContours(processed_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter and draw contours
    barcode_contour = None
    largest_area = 0
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = w / float(h)
        area = w * h

        # Filter contours based on area and aspect ratio
        if area > 500 and 1.5 < aspect_ratio < 10.0:  # Adjust thresholds as needed
            barcode_contour = contour
            largest_area = area
            cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Save the result
    output_path = "data/processed/05102009083_detected.jpg"
    cv2.imwrite(output_path, original_image)
    print(f"Detection result saved at: {output_path}")

    return barcode_contour
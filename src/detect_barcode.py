import cv2
import numpy as np
from pyzbar.pyzbar import decode

def detect_and_read_barcode(image_path):
    """
    Detect and read barcodes in the given image.
    """
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Compute the gradient in the x-direction
    gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradX = cv2.convertScaleAbs(gradX)

    # Blur the gradient and apply a binary threshold
    blurred = cv2.GaussianBlur(gradX, (9, 9), 0)
    _, thresh = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

    # Apply morphological operations to close gaps in the barcode
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # Remove small blobs and noise
    closed = cv2.erode(closed, None, iterations=4)
    closed = cv2.dilate(closed, None, iterations=4)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Sort contours by area and take the largest one
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)

        # Draw the bounding box on the original image
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Crop the barcode region
        barcode_region = gray[y:y+h, x:x+w]

        # Try to decode the barcode using pyzbar
        barcodes = decode(image)
        if barcodes:
            for barcode in barcodes:
                barcode_data = barcode.data.decode("utf-8")
                barcode_type = barcode.type
                print(f"Detected {barcode_type} barcode: {barcode_data}")

                # Draw the barcode data and type on the image
                cv2.putText(image, f"{barcode_data} ({barcode_type})", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        else:
            print("No barcode detected in the cropped region.")
    else:
        print("No contours detected for the barcode.")

    # Save the result
    output_path = "data/processed/detected_barcode2.jpg"
    cv2.imwrite(output_path, image)
    print(f"Detection result saved at: {output_path}")

# Example usage
if __name__ == "__main__":
    detect_and_read_barcode("data/raw/05102009083.jpg")
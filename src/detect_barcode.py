import cv2
import numpy as np

def detect_barcode(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    barcode_contour = max(contours, key=cv2.contourArea)
    
    x, y, w, h = cv2.boundingRect(barcode_contour)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Barcode Detected", img)
    cv2.waitKey(0)

if __name__ == "__main__":
    detect_barcode("data/raw/sample_image.jpg")
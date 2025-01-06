from pyzbar.pyzbar import decode
import cv2

def decode_barcode(image_path):
    img = cv2.imread(image_path)
    barcodes = decode(img)
    for barcode in barcodes:
        print("Decoded Data:", barcode.data.decode("utf-8"))

if __name__ == "__main__":
    decode_barcode("data/raw/sample_image.jpg")

from pyzbar.pyzbar import decode
import cv2

def decode_barcode(image):
    """
    Decode barcodes from the given image using pyzbar.
    """
    barcodes = decode(image)
    decoded_info = []
    for barcode in barcodes:
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type
        decoded_info.append((barcode_type, barcode_data))
    return decoded_info
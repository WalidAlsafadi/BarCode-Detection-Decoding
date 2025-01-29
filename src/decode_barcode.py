from pyzbar.pyzbar import decode
import cv2

def decode_barcode(image):
    """
    Decodes barcode(s) from an image.
    Returns a list of detected barcode data and their types.
    """
    barcodes = decode(image)
    decoded_info = []

    for barcode in barcodes:
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type
        decoded_info.append((barcode_type, barcode_data))

    return decoded_info
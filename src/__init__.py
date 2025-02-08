# Exposing key modules and functions for convenient imports
from .preprocess import preprocess_image
from .detect_barcode import detect_barcode
from .decode_barcode import decode_barcode
from .utils import ensure_directory_exists, get_file_name_without_extension, is_image_file

# Project metadata
__version__ = "1.0.0"
__author__ = "Walid Alsafadi & Ameer Alzerei"
__license__ = "Apache"
__email__ = "walid.k.alsafadi@gmail.com"
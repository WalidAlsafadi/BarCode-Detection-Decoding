# Barcode Detection and Decoding

This project provides an efficient solution for detecting and decoding barcodes from images using Python and OpenCV. It aims to process images, identify barcodes, and extract relevant information in a simple yet effective manner.

## Features

- **Barcode Detection**: Identifies barcodes in images by processing contours and enhancing visibility through Digital Image Processing (DIP).
- **Barcode Decoding**: Extracts and decodes barcode data (e.g., EAN13) from detected regions.
- **Flexible Design**: Easily extendable to support additional barcode formats.
- **Error Handling**: Comprehensive error detection and warnings during barcode processing.

## Project Structure

```
BarCode-Detection-Decoding/
├── data/
│   ├── annotations/
│   ├── processed/
│   └── raw/
├── docs/
│   ├── Project - Instructions.pdf
│   └── Efficient_Barcode_Detection_and_Decoding_Using_Digital_Image_Processing_Techniques.pdf
├── src/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── detect_barcode.py
│   ├── decode_barcode.py
│   ├── download_dataset.py
│   └── utils.py
├── tests/
│   ├── test_images/
│   ├── test_preprocess.py
│   ├── test_detect_barcode.py
│   ├── test_decode_barcode.py
│   └── test_pipeline.py
├── run_pipeline.py
├── requirements.txt
├── LICENSE
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/WalidAlsafadi/BarCode-Detection-Decoding.git
   cd BarCode-Detection-Decoding
   ```

2. Set up a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate       # On Linux/macOS
   venv\Scripts\activate          # On Windows
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the dataset (optional):
   Run the following script to automatically download the dataset:
   ```bash
   python src/download_dataset.py
   ```

   Alternatively, download the dataset manually from [Kaggle](https://www.kaggle.com/datasets/jonathanimmanuel/barcode-and-qr) and place it in the `data/raw/` directory.

## Usage

1. **Processing a Single Image**:
   ```bash
   python src/run_pipeline.py
   ```

   The results will be saved in the `data/processed/` directory.

2. **Running Tests**:
   Execute any test file directly:
   ```bash
   python tests/test_preprocess.py
   python tests/test_detect_barcode.py
   python tests/test_decode_barcode.py
   python tests/test_pipeline.py
   ```

3. **Customizing Paths**:
   Modify the `INPUT_DIR` and `OUTPUT_DIR` in `run_pipeline.py` to use different directories for raw and processed images.

## Testing

Unit tests are located in the `tests/` directory. Each test validates the functionality of individual modules:
- `test_preprocess.py`: Tests the image preprocessing pipeline.
- `test_detect_barcode.py`: Tests barcode detection.
- `test_decode_barcode.py`: Tests barcode decoding.
- `test_pipeline.py`: Tests the full pipeline from detection to decoding.

## Future Enhancements

- **Machine Learning Integration**: Upgrade from DIP to ML for handling blurred, rotated, or obscured barcodes more robustly.
- **UI Development**: Build a user interface for uploading images and visualizing detection and decoding results.
- **Real-Time Processing**: Extend to support live video or webcam barcode detection.

## Contributors

- **Walid Alsafadi**
- **Ameer Alzerei**

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
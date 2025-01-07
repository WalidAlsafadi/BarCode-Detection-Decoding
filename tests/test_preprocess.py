import os
import sys
import cv2

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from preprocess import preprocess_image

print("Starting test_preprocess.py...")

def test_preprocess_image():
    """
    Test the preprocess_image function.
    """
    # Path to the input image
    input_image_path = "data/raw/05102009083.jpg"  # Fix path (remove leading `/`)
    output_image_path = "data/processed/05102009083_processed.jpg"  # Fix path

    # Check if input image exists
    if not os.path.exists(input_image_path):
        print(f"Input image not found: {input_image_path}")
        return
    else:
        print(f"Input image found: {input_image_path}")

    # Run preprocessing
    print("Running preprocessing...")
    processed_image = preprocess_image(input_image_path)

    # DEBUG: Check if the processed image is valid
    if processed_image is None or processed_image.size == 0:
        print("Processed image is empty or None!")
        return
    else:
        print("Processed image generated successfully.")

    # Save the processed image
    print(f"Saving processed image to: {output_image_path}")
    success = cv2.imwrite(output_image_path, processed_image)
    if success:
        print(f"Processed image saved successfully at: {output_image_path}")
    else:
        print("Failed to save the processed image.")

    # Visualize contours
    visualize_contours(output_image_path)


def visualize_contours(processed_image_path):
    """
    Visualize all contours in the processed image and save the result.
    """
    processed_image = cv2.imread(processed_image_path, cv2.IMREAD_GRAYSCALE)
    contours, _ = cv2.findContours(processed_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contour_image = cv2.cvtColor(processed_image, cv2.COLOR_GRAY2BGR)  # Convert to color
    for contour in contours:
        cv2.drawContours(contour_image, [contour], -1, (0, 0, 255), 2)  # Red contours

    # Save the visualization
    contour_output_path = "data/processed/debug_contours.jpg"
    cv2.imwrite(contour_output_path, contour_image)
    print(f"Contours visualized and saved to: {contour_output_path}")


if __name__ == "__main__":
    test_preprocess_image()
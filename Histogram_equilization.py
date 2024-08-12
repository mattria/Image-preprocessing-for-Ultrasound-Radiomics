import cv2
import os

def ensure_directory_exists(directory):
    """Ensure the output directory exists, create if it doesn't."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def load_image_grayscale(image_path):
    """Load an image in grayscale mode."""
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Failed to load image: {image_path}")
    return image

def apply_histogram_equalization_and_save(image_path, output_path):
    """
    Apply histogram equalization to a grayscale image and save the result.

    :param image_path: Path to the input image.
    :param output_path: Path to save the enhanced image.
    """
    ensure_directory_exists(os.path.dirname(output_path))
    image = load_image_grayscale(image_path)
    hist_eq_image = cv2.equalizeHist(image)
    cv2.imwrite(output_path, hist_eq_image)
    print(f"Image enhanced with histogram equalization and saved to: {output_path}")

# Example usage
if __name__ == "__main__":
    input_image_path = 'input_images/example.jpg'
    output_image_path = 'output_images/example_hist_eq.jpg'
    apply_histogram_equalization_and_save(input_image_path, output_image_path)


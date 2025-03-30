import cv2
import os

def load_image(image_path):
    """
    Load the image from the specified file path.

    Args:
        image_path (str): Path to the image file.

    Returns:
        numpy.ndarray: Loaded image.

    Raises:
        FileNotFoundError: If the image file is not found.
        ValueError: If the image format is unsupported.
    """
    # Check if the file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Error: Image '{image_path}' not found.")

    # Explicitly reject unsupported formats like .heic
    if image_path.lower().endswith(".heic"):
        raise ValueError("Error: .heic files are not supported. Please use .jpg or .png files.")

    # Load the image using OpenCV
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Error: Unsupported image format for '{image_path}'.")
    return image

def preprocess_image(image):
    """
    Preprocess the image by converting it to grayscale and applying Gaussian blur.

    Args:
        image (numpy.ndarray): Input image.

    Returns:
        tuple: Grayscale image and blurred image.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    return gray, blurred
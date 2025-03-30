import cv2

def detect_edges(blurred_image):
    """
    Apply the Canny edge detection algorithm to the blurred image.

    Args:
        blurred_image (numpy.ndarray): Input blurred image.

    Returns:
        numpy.ndarray: Image with edges detected.
    """
    edges = cv2.Canny(blurred_image, 50, 150)
    return edges
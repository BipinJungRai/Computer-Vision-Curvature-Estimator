import numpy as np
import cv2

# This file handles contour-related operations:
# 1. Finds the largest contour in an edge-detected image.
# 2. Estimates the curvature of a contour.

def find_largest_contour(edges):
    """
    Find the largest contour in an edge-detected image.

    Args:
        edges (numpy.ndarray): Edge-detected image.

    Returns:
        numpy.ndarray: The largest contour based on area.

    Raises:
        ValueError: If no contours are found in the image.
    """
    # Find all contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # Raise an error if no contours are found
    if not contours:
        raise ValueError("No contours found.")
    # Return the largest contour based on area
    return max(contours, key=cv2.contourArea)

def estimate_curvature(contour, window=5):
    """
    Estimate the curvature of a contour using a sliding window approach.

    Args:
        contour (numpy.ndarray): Contour points.
        window (int): Number of points on either side of the current point to consider. Defaults to 5.

    Returns:
        tuple: A tuple containing:
            - points (list of tuple): List of (x, y) coordinates of the contour points.
            - curvatures (list of float): List of curvature values for the corresponding points.
    """
    # Initialize lists to store curvature values and points
    curvatures = []
    points = []

    # Iterate through the contour points with a sliding window
    for i in range(window, len(contour) - window):
        # Extract three points: previous, current, and next
        p1 = contour[i - window][0]
        p2 = contour[i][0]
        p3 = contour[i + window][0]

        # Calculate vectors between the points
        v1 = p1 - p2
        v2 = p3 - p2

        # Calculate the dot product and magnitudes of the vectors
        dot = np.dot(v1, v2)
        mag = np.linalg.norm(v1) * np.linalg.norm(v2)
        # Calculate the curvature based on the angle between the vectors
        if mag == 0:
            curvature = 0
        else:
            angle = np.arccos(np.clip(dot / mag, -1.0, 1.0))
            curvature = np.pi - angle  # Higher values indicate sharper bends

        # Append the curvature and the current point
        curvatures.append(curvature)
        points.append(p2)

    # Return the points and their corresponding curvature values
    return points, curvatures
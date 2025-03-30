import cv2
import numpy as np

# This file handles visualization of the results:
# 1. Displays the original image, grayscale image, edges, and curvature visualization.
# 2. Draws circles on the image based on curvature intensity.

def visualize_results(image, gray, edges, points, curvatures):
    # Create a copy of the original image to draw on
    output = image.copy()
    
    # Iterate through points and their corresponding curvatures
    for pt, curv in zip(points, curvatures):
        x, y = pt  # Extract x and y coordinates of the point
        # Calculate intensity based on curvature, scaled to 0-255
        intensity = int(min(curv * 255 / np.pi, 255))
        # Draw a circle at the point with color based on curvature intensity
        cv2.circle(output, (x, y), 2, (0, intensity, 255 - intensity), -1)

    # Display the original image
    cv2.imshow("Original", image)
    # Display the grayscale version of the image
    cv2.imshow("Grayscale", gray)
    # Display the edges detected in the image
    cv2.imshow("Edges", edges)
    # Display the image with curvature estimation visualization
    cv2.imshow("Curvature Estimation", output)
    
    # Wait for a key press to close the windows
    cv2.waitKey(0)
    # Close all OpenCV windows
    cv2.destroyAllWindows()
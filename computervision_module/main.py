import os
import cv2
import numpy as np
from image_loader import load_image, preprocess_image
from edge_detector import detect_edges
from contour_utils import find_largest_contour, estimate_curvature
from csv_writer import save_curvature_to_csv
from visualizer import visualize_results
from curvature_converter import convert_curvature_to_meters

def main():
    """
    Main entry point of the program. It orchestrates the workflow:
    1. Load and preprocess the image.
    2. Allow the user to select a region of interest (ROI).
    3. Detect edges and find the largest contour in the ROI.
    4. Estimate curvature and save results to a CSV file.
    5. Visualize the results.
    """
    # Locate the computervision_module directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    test_image_folder = os.path.join(base_dir, 'test_image')

    # Ensure the test_image folder exists
    if not os.path.exists(test_image_folder):
        raise FileNotFoundError(f"The folder 'test_image' was not found in {base_dir}. Please create it and add images.")

    # List all available images in the test_image folder
    print("\n" + "="*50)
    print("Available images in 'test_image' folder:")
    available_images = [f for f in os.listdir(test_image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not available_images:
        raise FileNotFoundError(f"No images found in the folder: {test_image_folder}")

    # Display the list of images with corresponding numbers
    for idx, img_name in enumerate(available_images, start=1):
        print(f"{idx}. {img_name}")
    print("="*50)

    # Prompt the user to select an image
    while True:
        try:
            image_choice = int(input("Enter the number corresponding to the image you want to process: "))
            if 1 <= image_choice <= len(available_images):
                image_name = available_images[image_choice - 1]
                break
            else:
                print(f"Please enter a number between 1 and {len(available_images)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Construct the full path to the selected image
    image_path = os.path.join(test_image_folder, image_name)
    print(f"Selected image: {image_name}")

    # Define camera parameters TODO: Update these values based on your camera setup in franka Lab
    camera_height_m = 1.5  # Camera height from the table in meters
    focal_length_mm = 35.0  # Camera focal length in mm
    sensor_width_mm = 36.0  # Camera sensor width in mm

    # Extract the image name (without extension) for saving results
    image_name_no_ext = os.path.splitext(image_name)[0]

    # Step 1: Load the image
    image = load_image(image_path)

    # Step 2: Allow the user to select a region of interest (ROI)
    print("\n" + "="*50)
    print("Instructions for ROI Selection:")
    print("- Use the mouse to draw a rectangle over the region of interest.")
    print("- You can reposition or redraw the rectangle as needed.")
    print("- Press ENTER or SPACE to confirm the selection.")
    print("- Press ESC to cancel the selection.")
    print("="*50)
    
    # Display the image with a descriptive window title
    window_title = "Select ROI - Draw a rectangle and press ENTER or SPACE to confirm"
    roi = cv2.selectROI(window_title, image)
    cv2.destroyWindow(window_title)  # Close the ROI selection window automatically

    # Crop the image to the selected ROI
    x, y, w, h = map(int, roi)
    cropped_image = image[y:y+h, x:x+w]

    # Step 3: Preprocess the cropped image (convert to grayscale and apply Gaussian blur)
    gray, blurred = preprocess_image(cropped_image)

    # Step 4: Detect edges in the preprocessed image
    edges = detect_edges(blurred)

    # Step 5: Find the largest contour in the edge-detected image
    contour = find_largest_contour(edges)

    # Step 6: Estimate the curvature of the largest contour
    points, curvatures = estimate_curvature(contour, window=5)

    # Step 6.1: Convert curvature from pixels^-1 to meters^-1
    image_width_px = image.shape[1]
    curvatures_meters, pixels_per_meter = convert_curvature_to_meters(
        curvatures, camera_height_m, focal_length_mm, sensor_width_mm, image_width_px
    )
    print(f"Conversion factor (pixels_per_meter): {pixels_per_meter:.4f}")

    # Step 7: Save the curvature data (points and curvatures) to a CSV file
    csv_path = save_curvature_to_csv(
        points, 
        curvatures_meters, 
        image_name_no_ext, 
        camera_height_m, 
        focal_length_mm, 
        sensor_width_mm, 
        pixels_per_meter
    )
    
    # Step 8: Print curvature statistics (mean and maximum curvature)
    print("\n" + "="*50)
    print("Processing Results:")
    print(f"Curvature data saved to: {csv_path}")
    print(f"Mean Curvature (meters^-1): {np.mean(curvatures_meters):.4f}")
    print(f"Max Curvature (meters^-1): {np.max(curvatures_meters):.4f}")
    print(f"Mean Curvature (pixels^-1): {np.mean(curvatures):.4f}")
    print(f"Max Curvature (pixels^-1): {np.max(curvatures):.4f}")
    print("="*50)

    # Step 9: Visualize the results (original image, grayscale, edges, and curvature)
    visualize_results(cropped_image, gray, edges, points, curvatures_meters)

if __name__ == "__main__":
    """
    Entry point of the script.
    """
    main()
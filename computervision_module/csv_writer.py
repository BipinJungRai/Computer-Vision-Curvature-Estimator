import os
import csv

def save_curvature_to_csv(points, curvatures, image_name, camera_height_m, focal_length_mm, sensor_width_mm, pixels_per_meter):
    """
    Saves curvature data (points and their corresponding curvature values) to a CSV file.

    This function writes the curvature data, along with metadata such as camera parameters
    and summary statistics, to a CSV file for further analysis.

    Args:
        points (list of tuple): A list of (x, y) coordinates of the points on the contour.
        curvatures (list of float): A list of curvature values (in meters^-1) corresponding to the points.
        image_name (str): The name of the image (used for naming the CSV file).
        camera_height_m (float): The height of the camera from the table, in meters.
        focal_length_mm (float): The focal length of the camera, in millimeters.
        sensor_width_mm (float): The width of the camera sensor, in millimeters.
        pixels_per_meter (float): The conversion factor from pixels to meters.

    Returns:
        str: The path to the saved CSV file.
    """
    # Locate the computervision_module directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(base_dir, 'csv_output')

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Define the path to the CSV file
    csv_path = os.path.join(output_folder, f"{image_name}.csv")

    # Open the CSV file for writing
    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        # Write metadata as comments (can comment out if not needed)
        writer.writerow([f"# Image Name: {image_name}"])
        writer.writerow([f"# Camera Height (meters): {camera_height_m}"])
        writer.writerow([f"# Focal Length (mm): {focal_length_mm}"])
        writer.writerow([f"# Sensor Width (mm): {sensor_width_mm}"])
        writer.writerow([f"# Conversion Factor (pixels_per_meter): {pixels_per_meter:.4f}"])
        writer.writerow([])  # Add an empty row for separation
        # Write the header row
        writer.writerow(["x (pixels)", "y (pixels)", "curvature (meters^-1)"])
        # Write each point and its curvature value
        for (x, y), c in zip(points, curvatures):
            writer.writerow([x, y, c])
        # Write summary statistics at the end of the file
        mean_curvature = sum(curvatures) / len(curvatures)
        max_curvature = max(curvatures)
        writer.writerow([])  # Add an empty row for separation
        writer.writerow(["# Summary Statistics"])
        writer.writerow([f"# Mean Curvature (meters^-1): {mean_curvature:.4f}"])
        writer.writerow([f"# Max Curvature (meters^-1): {max_curvature:.4f}"])
    
    # Return the path to the saved CSV file
    return csv_path
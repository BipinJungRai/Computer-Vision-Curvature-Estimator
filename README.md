# Computer Vision Curvature Analysis

This project is a Python-based tool for analyzing the curvature of contours in images. It processes an input image, detects edges, identifies the largest contour, estimates its curvature, and visualizes the results. Additionally, the curvature data is saved to a CSV file for further analysis.

## Features
1. **Image Loading and Preprocessing**: Converts the input image to grayscale and applies Gaussian blur.
2. **Edge Detection**: Uses the Canny edge detection algorithm to identify edges in the image.
3. **Contour Analysis**: Finds the largest contour and estimates its curvature.
4. **Data Export**: Saves the curvature data (points and curvature values) to a CSV file.
5. **Visualization**: Displays the original image, grayscale image, edges, and curvature visualization.

## File Structure
- `main.py`: Orchestrates the workflow of the program.
- `image_loader.py`: Handles image loading and preprocessing.
- `edge_detector.py`: Performs edge detection using the Canny algorithm.
- `contour_utils.py`: Finds the largest contour and estimates its curvature.
- `csv_writer.py`: Saves curvature data to a CSV file.
- `visualizer.py`: Visualizes the results.
- `curvature_converter.py`: Converts curvature values from pixels to meters.

## How to Use

### Prerequisites
- Python 3.12 or higher
- Required Python libraries:
  - `numpy`
  - `opencv-python`

### Installation
1. Clone this repository to your local machine.
2. Install the required libraries using the following command:

   ```bash
   pip install -r requirements.txt
   ```

### Steps to Run the Program
1. **Prepare the Input Image**:
   - Place the image you want to analyze in the `test_image` folder.
   - Ensure the image is in a supported format (e.g., `.jpg` or `.png`).

2. **Set Camera Parameters**:
   - Open the `main.py` file.
   - Update the following variables with your camera's specifications:
     - `camera_height_m`: Height of the camera from the table in meters.
     - `focal_length_mm`: Focal length of the camera in millimeters.
     - `sensor_width_mm`: Width of the camera sensor in millimeters.

3. **Specify the Input Image**:
   - In `main.py`, update the `image_path` variable with the name of your image file (e.g., `test_image/your_image.jpg`).

4. **Run the Program**:
   - Execute the `main.py` script using the following command:

     ```bash
     python main.py
     ```

5. **Select the Region of Interest (ROI)**:
   - Follow the on-screen instructions to draw a rectangle over the region of interest in the image.
   - Press `ENTER` or `SPACE` to confirm the selection, or `ESC` to cancel.

6. **View Results**:
   - The program will process the image, estimate the curvature, and save the results to a CSV file in the `csv_output` folder.
   - It will also display visualizations of the original image, grayscale image, edges, and curvature estimation.

7. **Analyze the Output**:
   - Open the generated CSV file in the `csv_output` folder to view the curvature data and summary statistics.
   - Use the visualizations to interpret the curvature results.

### Example
If your input image is named `banana.jpg`, place it in the `test_image` folder and set `image_path` in `main.py` as follows:

```python
image_path = 'test_image/banana.jpg'
```

Then, run the program and follow the instructions to analyze the curvature.
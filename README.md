# Computer Vision Curvature Estimator

A Python-based application for estimating and analyzing curvature from images using computer vision techniques. This tool is designed for researchers, engineers, and developers working on image processing, robotics, or related fields.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Dependencies](#dependencies)
7. [Contributing](#contributing)
8. [License](#license)

---

## Overview

The **Computer Vision Curvature Estimator** processes images to detect edges, extract contours, and compute curvature values. It outputs the results in a CSV file and provides visualization for better analysis. This project is modular, making it easy to extend or integrate into larger systems.

---

## Features

- **Image Preprocessing**: Load and preprocess images for analysis.
- **Edge Detection**: Detect edges using advanced computer vision techniques.
- **Contour Analysis**: Extract the largest contour and compute curvature values.
- **Curvature Conversion**: Convert curvature values to real-world units.
- **CSV Export**: Save curvature data and metadata to a CSV file.
- **Visualization**: Visualize contours and curvature for better understanding.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Computer-Vision-Curvature-Estimator.git
   cd Computer-Vision-Curvature-Estimator
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r computervision_module/requirements.txt
   ```

---

## Usage

1. Place your input image in the `computervision_module/test_image/` directory.
2. Run the main script:
   ```bash
   python computervision_module/main.py
   ```
3. The processed results will be saved in:
   - **CSV Output**: `computervision_module/csv_output/`
   - **Visualization**: Displayed on the screen.

4. Close the OpenCV windows by pressing the `q` key.

---

## Project Structure

```
Computer-Vision-Curvature-Estimator/
├── README.md
├── computervision_module/
│   ├── contour_utils.py         # Contour extraction and curvature estimation
│   ├── csv_writer.py            # Save curvature data to CSV
│   ├── curvature_converter.py   # Convert curvature to real-world units
│   ├── edge_detector.py         # Edge detection logic
│   ├── image_loader.py          # Image loading and preprocessing
│   ├── main.py                  # Main entry point of the application
│   ├── requirements.txt         # Python dependencies
│   ├── visualizer.py            # Visualization of results
│   ├── csv_output/              # Directory for CSV outputs
│   └── test_image/              # Directory for input images
```

---

## Dependencies

The project uses the following Python libraries:
- `numpy`
- `opencv-python`
- `matplotlib`

Install all dependencies using the `requirements.txt` file:
```bash
pip install -r computervision_module/requirements.txt
```

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your fork:
   ```bash
   git commit -m "Add feature-name"
   git push origin feature-name
   ```
4. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or feedback, please contact:
- **Name**: Your Name
- **Email**: your.email@example.com
- **GitHub**: [your-username](https://github.com/your-username)
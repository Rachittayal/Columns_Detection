# Columns Detection

This project focuses on detecting and extracting pillars/columns from an image, representing each column with a unique color, and saving the boundaries of the detected pillars as a set of points. It uses image processing techniques such as edge detection, contour detection, and visualization to achieve the desired results.

## Introduction

The goal of this project is to identify and process pillars/columns present in an image, detect their boundaries, and output the points corresponding to each pillar. The pillars are represented with different colors, and the boundaries are saved as text files containing the coordinates of these points.

### Directories and Files:

- **input/**: Contains the input image file (`image.jpg`) to process.
- **output/**: Contains the output image and the points for each detected pillar, stored as `.txt` files.
- **src/**: Contains the core image processing scripts (preprocessing, edge detection, contour detection, and visualization).
- **main.py**: The main script to run the entire processing pipeline.
- **requirements.txt**: Lists all the required Python packages to run the project.

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Columns_Detection.git
cd Columns_Detection  

2. Create a Virtual Environment (Optional but recommended)
It's recommended to use a virtual environment to isolate dependencies. You can create one using the following commands:

python -m venv senv
source senv/bin/activate  # For macOS/Linux
senv\Scripts\activate     # For Windows

3. Install Dependencies
Once the virtual environment is activated, install the required dependencies from requirements.txt:

pip install -r requirements.txt
To run the pipeline, execute the main.py script:
python main.py

This will process the input image (input/image.jpg), detect the pillars, and save the output in the output/ directory, including:

The final processed image (result.jpg) with colored pillars.
.txt files containing the boundary points for each pillar (e.g., pillar_1.txt, pillar_2.txt, etc.).
File Descriptions
input/image.jpg: The input image containing pillars to be detected.
output/result.jpg: The output image with pillars highlighted in different colors.
output/pillar_1.txt, pillar_2.txt, ...: Text files containing the coordinates of the boundaries of each detected pillar.
src/preprocess.py: Contains functions for image preprocessing (resizing, blurring, etc.).
src/edges.py: Handles edge detection using algorithms like Canny edge detection.
src/contours.py: Detects contours and groups the points corresponding to each pillar.
src/visualize.py: Contains functions for visualizing the results and saving the processed image and points.
Dependencies
This project requires the following Python libraries:

opencv-python: For image processing and visualization.
numpy: For numerical operations and handling arrays.
matplotlib: For plotting and visualizing images.
scipy: For scientific operations.
These are specified in the requirements.txt file. To install them, run:

pip install -r requirements.txt


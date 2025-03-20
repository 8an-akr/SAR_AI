### SAR AI - Synthetic Aperture Radar Object Detection and Terrain Classification
## Overview
This project aims to detect multiple vehicle types and classify terrain types in Synthetic Aperture Radar (SAR) images using YOLOv8. The model is trained on synthetic composite images that combine vehicle images from the MSTAR dataset with realistic SAR background images from the Sentinel-1/2 dataset. The goal is to recognize and localize various military vehicles and determine the terrain type.

## Features
# Synthetic Image Generation:

Combines multiple SAR vehicle images on realistic terrain backgrounds.
Supports various terrains: agricultural, barren land, grassland, and urban.
Generates labeled composite images for training.
Training and Detection with YOLOv8:

Uses YOLOv8 for object detection and terrain classification.
Automatically trains on synthetic images.
Fine-tunes the model to recognize both vehicles and terrain types.
Visualization:

Displays bounding boxes and labels on detected objects and terrains.
Provides visual verification of detection accuracy.
Automatic Data Handling and Caching:

Downloads datasets from Kaggle if not already present.
Caches processed data to avoid redundant operations.
Saves models and results directly to the GitHub repository for persistence.
Installation
To run the Colab notebook, ensure you have the following libraries:

gitpython for handling Git operations.
wget for downloading files.
ultralytics for YOLOv8 support.
PIL for image manipulation.
torch for model training and inference.
Install the required packages using:

python
Copy
Edit
!pip install gitpython wget ultralytics
Usage
Clone the repository:
bash
Copy
Edit
git clone https://github.com/8an-akr/SAR_AI.git
cd SAR_AI
Open and run the Colab notebook:
Follow the instructions to set up the environment and download datasets.
Train the YOLOv8 model on synthetic images.
Run inference to detect vehicles and terrain types.
Visualize results with bounding boxes.
Datasets
MSTAR Dataset (Vehicles):

Downloaded from Kaggle.
Includes 8 classes of military vehicles.
Sentinel-1/2 SAR Backgrounds:

Includes terrain categories like agricultural, barren land, grassland, and urban.
Results
After training, the model:

Detects vehicles and predicts their types.
Classifies terrain based on background images.
Visualizes detection with bounding boxes and labels.
Saving and Pushing Results
The model, generated data, and results are automatically pushed to the GitHub repository for future use and analysis.

Acknowledgements
Special thanks to the creators of the MSTAR and Sentinel-1/2 datasets for providing the valuable data that made this project possible.


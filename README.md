# Face Recognition Using PCA and K-NN Algorithms

## Description

The "Face Recognition Using PCA and K-NN Algorithms" project is a Python-based application that utilizes Principal Component Analysis (PCA) and K-Nearest Neighbors (K-NN) algorithms to recognize faces from images. The project aims to provide a reliable and efficient solution for face recognition tasks, such as identifying individuals from a database of images or detecting known faces in real-time video streams.

This is implemented in Python and utilizes popular libraries such as OpenCV, NumPy, and scikit-learn for image processing, matrix operations, and machine learning tasks

## Features

- Captures images of people for training, and these images are automatically converted to grayscale with a size of 224x224 pixels.
- Manually, you can train a dataset and save the data to files (pca.pkl, trainDataS.pkl, trainDataS.csv.
- Performs real-time face recognition using K-nearest neighbors (KNN) classifier with PCA for dimensionality reduction on camera frames

## Prerequisites

- Python 3 installed on your system

## Installation

To get started with the face recognition project, follow these steps:

- Clone the GitHub repository:  
  `git clone https://github.com/hexa2525/face_recognition-pca-knn.git`
- Navigate to the project directory:  
  `cd face_recognition-pca-knn`
- Install the required dependencies using pip:  
   `python3 -m pip install -r requirements.txt
`

# Usage

- Navigate to the project directory: `cd face_recognition-pca-knn`

- Simply run `python3 face_reco.py`

## Dependencies

- customtkinter==5.1.2
- pandas==1.5.3
- scikit-learn: 0.24.2 or higher
- numpy: 1.19.5 or higher
- OpenCV: 4.5.2 or higher


## License

[MIT licensed](./LICENSE).
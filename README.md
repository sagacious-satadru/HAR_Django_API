# Human Activity Recognition (HAR) Django API

This repository contains a Django-based web application that uses a machine learning model to classify human activities based on images. The model was trained using the images downloaded via the Bing Image search API. 

## Features

- Upload an image through a simple web interface.
- The image is processed and fed into a pre-trained machine learning model.
- The model predicts the human activity in the image.
- The application displays the predicted activity classes in descending order of their confidence level of prediction.

## Installation

1. Clone this repository to your local machine using `git clone https://github.com/sagacious-satadru/HAR_Django_API.git`.
2. Navigate to the project directory: `cd HAR_Django_API`.
3. Install the required Python packages: `pip install -r requirements.txt`.
4. Run the Django server: `python manage.py runserver`.
5. Open your web browser and navigate to `http://localhost:8000` to use the application.

## Usage

1. Click the "Upload" button to select an image from your local machine.
2. Click "Submit" to send the image to the server.
3. The server will process the image and display the predicted human activity with the highest confidence level at the top, along with its confidence level, followed by the other classes of human activities with lower confidence levels, which thus have a lower possibility of being true for the given image.

### The notebook is a part of the final project done for Celebal Summer Internship 2023 - by Satadru Bhowmik (CSI ID:  CT-CSI23/DS0492)


Here's the link to that notebook in which I trained the model that has been utilized here: [Notebook Link](https://github.com/sagacious-satadru/Human_Activity_Recognition_FastAI)

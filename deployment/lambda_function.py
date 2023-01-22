#!/usr/bin/env python
# coding: utf-8

# Required libraries
import json
import urllib.request
import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor



# List of classes
classes = ['fire', 'nofire']

# Image url
img_url = 'https://ichef.bbci.co.uk/news/976/cpsprodpb/32A5/production/_123456921_australianbushfire_gettyimages-1198540877.jpg'


# Initalize interpreter
interpreter = tflite.Interpreter(model_path='wildfire-model.tflite')
# Allocate memory
interpreter.allocate_tensors()
# Get the input index from interpreter
input_index = interpreter.get_input_details()[0]['index']
# Get the output index from interpreter
output_index = interpreter.get_output_details()[0]['index']


# Function to preprocess image (image from url)
def img_preprocess(img_url):
    # Create preprocessor for the model we used for training (Xception)
    preprocessor = create_preprocessor('xception', target_size=(299, 299))
    # Preprocess the image
    X = preprocessor.from_url(img_url)
    return X


# Function to make predictions on image url
def predict(img_url):
    # Preprocess the image
    X = img_preprocess(img_url)
    # Get image predictions from tensors
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)[0]

    # Convert numpy array predictions into float type
    # for conversion we simply need to convert array to python list first
    float_preds = preds.tolist()
    return dict(zip(classes, float_preds))


# Function to create lambda handler
def lambda_handler(event, context):
    try:
        img_url = event['url']
        result = predict(img_url)
        
        # Get the predicted class name from result dictionary
        pred_class = max(result, key=result.get)
        return pred_class
    except ValueError as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": e.args[0]})
        }
    except urllib.error.URLError as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid URL provided, please check the URL format"})
        }









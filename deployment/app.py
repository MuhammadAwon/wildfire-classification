import os
import requests
import gradio as gr

from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
from urllib.request import urlopen

# Load environment variable
load_dotenv()
api = os.getenv('API')


# Function to display image and predicted class
def display_image(url):
    image_data = urlopen(url).read()
    image = Image.open(BytesIO(image_data))
    api_url = api
    json_data = {'url': url}
    response = requests.post(api_url, json=json_data)
    prediction = response.content.decode().strip("\"")
    return image, prediction

iface = gr.Interface(fn=display_image, inputs="text", outputs=["image", gr.outputs.Label(num_top_classes=2)],
                     description="Enter image url (*image of wildfire* or *image of no wildfire*) and it will be displayed with prediction.")
iface.launch()

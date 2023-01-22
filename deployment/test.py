import os
import requests
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()

# API endpoint
API = os.getenv('API')

# # Local host endpoint to send request
# url = 'http://localhost:8080/2015-03-31/functions/function/invocations'


# Image url (fire)
img_url = 'https://ichef.bbci.co.uk/news/976/cpsprodpb/32A5/production/_123456921_australianbushfire_gettyimages-1198540877.jpg'

# Image url (nofire)
img_url2 = 'https://thumbs.dreamstime.com/b/aerial-view-lago-antorno-dolomites-lake-mountain-landscape-alps-peak-misurina-cortina-di-ampezzo-italy-reflected-103752677.jpg'

# Set the headers for the POST request
headers = {'Content-Type': 'application/json'}

# Set the data for the POST
data = {'url': img_url}

# Send the POST request as json
response = requests.post(API, json=data, headers=headers)

# Parse response in to json
print(response.json())


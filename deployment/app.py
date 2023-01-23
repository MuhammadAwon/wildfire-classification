import os
import base64
import requests
import streamlit as st
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
from urllib.request import urlopen



# Load environment variable
load_dotenv()
api = os.getenv('API')


# Function to display background image
def add_bg_from_local(image_file):
    with open(image_file, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{'jpg'};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('bg-img.jpg')


# Description of the classes (fire, nofire)
desc_fire = """<span style='color:#d94c00'>The predicted class is "fire", indicating that the image contains signs of a wildfire. Wildfires are uncontrolled fires that burn through forests, grasslands, and other natural areas.
They can be caused by a variety of factors, including lightning strikes, human activity, and drought.
Wildfires can have a devastating impact on the environment and communities, destroying homes and habitats,
and causing air pollution and health problems.</span>

<span style='color:#d94c00'>This [website](https://www.who.int/health-topics/wildfires#tab=tab_1) is the World Health Organization's (WHO) page on the topic of wildfires.
The website provides information on the health effects of wildfires, including the risks to respiratory and cardiovascular health,
as well as the impacts on mental health. It also provides guidance on how to protect yourself and your community during a wildfire,
including tips on how to reduce exposure to smoke and ash.
Additionally, the website provides information on how to prepare for and respond to a wildfire,
including emergency planning and evacuation.</span>
"""

desc_nofire = """<span style='color:#add8e6'>The predicted class is "nofire", which means that there is no wildfire present in the image.
This is excellent news and allows for safe exploration and enjoyment of the natural beauty around us.
Without the threat of fire, we can fully immerse ourselves in the natural world and appreciate all it has to offer.</span>

<span style='color:#add8e6'>Speaking of exploring the world, have you heard of [Lindblad Expedition](https://world.expeditions.com/)?
This website offers a wide range of adventure trips to some of the most beautiful and remote places on Earth.
Whether you're an experienced traveler or just starting out, they have something for everyone.
From hiking in the Himalayas to diving in the Great Barrier Reef, there's a trip that will suit your interests and abilities.</span>

<span style='color:#add8e6'>What sets [Lindblad Expedition](https://world.expeditions.com/) apart is their commitment to sustainable travel.
They work with local communities and organizations to minimize their impact on the environment and
ensure that the money spent on their trips goes back into the local economy.</span>

<span style='color:#add8e6'>So if you're looking for an adventure that will take you off the beaten path and give you an authentic experience of the world,
look no further than [Lindblad Expedition](https://world.expeditions.com/).
With them, you can explore the world in a whole new way and make a positive impact on the places you visit.</span>
"""


# Function to display image and predicted class from image url
def display_image(url):
    image_data = urlopen(url).read()
    image = Image.open(BytesIO(image_data))
    api_url = api
    json_data = {'url': url}
    response = requests.post(api_url, json=json_data)
    prediction = response.content.decode().strip('\"') # decode the byte string from response (e.g, b'"fire"')
    return image, prediction


# st.title("Wildfire Image Classification App")
st.markdown('<h1 style="color: white;">Wildfire Image Classification App</h1>', unsafe_allow_html=True)

# Input image url
url = st.text_input(':orange[Enter image URL: ]')

# Display image and predicted class
if st.button('Submit') and url:
    image, prediction = display_image(url)
    # Display image
    st.image(image, use_column_width=True)
    st.write('<div style="text-align: center; color: lightgrey">Displayed Image</div>', unsafe_allow_html=True)
    # Display prediction
    if prediction == 'fire':
        st.write(f'<span>{desc_fire}</span>', unsafe_allow_html=True)
    elif prediction == 'nofire':
        st.markdown(f'<span>{desc_nofire}</span>', unsafe_allow_html=True)

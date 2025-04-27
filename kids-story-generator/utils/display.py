import requests
from PIL import Image
from io import BytesIO

def display_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

def save_image_from_url(url, filename="assets/generated_image.png"):
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)

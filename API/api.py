import requests
from nasapy import Nasa
from PIL import Image

def gifer(images):
    images[0].save('earth.gif', save_all=True, append_images=images[1:], optimize=True, duration=100, loop=0)

api_key = "WBBca38ISfYUgHZdDdval5aJFqZNcYzyj7BsNQf5"

search_date = input('Введите дату в формате "ГГГГ"-"MM-"ДД":')

nasa = Nasa(key=api_key)
images_data = nasa.epic(date = search_date)
image_count = 0

image_to_gif = []

for image in images_data:
    url = f'https://api.nasa.gov/EPIC/archive/natural/{search_date.replace("-","/")}/png/{image["image"]}.png?api_key={api_key}'

    response = requests.get(url)
    response.raise_for_status()

    image_count += 1
    with open(f'image{image_count}.png','wb') as img:
        img.write(response.content)
        image_to_gif.append(Image.open(f'image{image_count}.png'))


gifer(image_to_gif)
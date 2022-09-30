from fileinput import filename
import random as _random
import requests as _requests
import os as _os
import dotenv as _dotenv
import constants as _constants

_dotenv.load_dotenv()

ACCESS_KEY = _os.environ['ACCESS_KEY']

def _search_images():
    query = _random.choice(_constants.UNSPLASH_QUERIES)
    url = f'https://api.unsplash.com/search/photos?page=1&query={query}&client_id={ACCESS_KEY}'
    response = _requests.get(url)

    data = response.json()['results']
    return data

def _get_random_img_link():
    response_data = _search_images()
    random_image_data = _random.choice(response_data)
    link = random_image_data['urls']['regular']
    return link

def download_image():
    filename = 'picture.jpg'
    image_url = _get_random_img_link()
    image_response = _requests.get(image_url, stream=True)
    if image_response.status_code == 200:
        with open(filename, 'wb') as image:
            for chunck in image_response:
                image.write(chunck)


download_image()
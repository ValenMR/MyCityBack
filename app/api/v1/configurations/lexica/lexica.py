from random import randint
from fastapi import status
import requests
from .....environment import LEXICA_URL

def get_random_image(image_name: str) -> str:
    url = f"{LEXICA_URL}?q={image_name}"
    result = requests.get(url)

    if result.status_code == status.HTTP_200_OK:
        data = result.json()
        position = randint(0, len(data["images"])) - 1
        image_url = data["images"][position]["src"]
        return image_url
        
    return ""
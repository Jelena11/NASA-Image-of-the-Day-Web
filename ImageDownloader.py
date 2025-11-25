import os
import requests
import json

def get_data(api_key):
    raw_response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}').text
    response = json.loads(raw_response)
    return response

def get_date(response):
    date = response['date']
    return date

def get_url(response):
    url = response['url']
    return url

def get_explaination(response):
    explaination = response['explanation']
    return explaination

def download_image(url, date):
    if os.path.isfile(f'{date}.png') == False:
        raw_image = requests.get(url).content
        with open(f'{date}.jpg', 'wb') as file:
            file.write(raw_image)

    else:
        return FileExistsError
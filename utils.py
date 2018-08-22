import os
import requests

from pprint import pprint


def send_email(**kwargs):
    print("Sent email to {0}".format(kwargs.get('to')))
    pprint(kwargs)


def save_image_from_internet(url):
    if not url:
        return None
    response = requests.get(url)
    filepath = '/home/rtownley/Pictures'
    filename = url.split('/')[-1]
    fileurl = os.path.join(filepath, filename)
    if response.status_code == 200 and not os.path.isfile(fileurl):
        with open(fileurl, 'wb') as f:
            f.write(response.content)

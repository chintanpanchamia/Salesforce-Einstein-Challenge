# __author__ = 'chintanpanchamia'
import requests
from constants import EINSTEIN_VISION_URL


def generate_token(assertion):
    url = EINSTEIN_VISION_URL+"/v1/oauth2/token"
    data = {
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": assertion
    }

    try:
        response = requests.post(url, data=data)
        return response
    except requests.exceptions.RequestException as exp:
        raise exp  # ("Token generation failed: \"{}\"".format(response))

# __author__ = 'chintanpanchamia'
import imghdr
import requests
from constants import EINSTEIN_VISION_URL


file_types = {
    'png': '/image/png',
    'jpg': '/image/jpg',
    'jpeg': '/image/jpeg',
}

prediction_url = '{0}/v1/vision/predict'.format(EINSTEIN_VISION_URL)


def predict_with_url(token, model_id, image_url):
    payload = {
        'sampleLocation': (None, image_url),
        'model_id': (None, model_id),
    }

    headers = {
        'Authorization': 'Bearer %s' % token,
        'Cache-Control': 'no-cache',
    }

    return prediction_request(prediction_url, payload, headers)


def prediction_with_image_file(token, model_id, image_file_path):
    payload = {
        'sampleContent': ('image', open(image_file_path), file_types[get_file_type(image_file_path)]),
        'model_id': (None, model_id)
    }

    headers = {
        'Authorization': 'Bearer %s' % token,
        'Cache-Control': 'no-cache',
    }

    return prediction_request(prediction_url, payload=payload, headers=headers)


def prediction_request(url, payload, headers):
    try:
        response = requests.post(url, files=payload, headers=headers)
        return response
    except requests.exceptions.RequestException as e:
        raise e


def get_file_type(file_path):
    try:
        return imghdr.what(file_path)
    except IOError as e:
        raise e

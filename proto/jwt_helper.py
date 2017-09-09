# __author__ = 'chintanpanchamia'
import jwt
from constants import EINSTEIN_VISION_URL


def generate_assertion(subject, private_key, expiry):
    url = '{0}/v1/oauth2/token'.format(EINSTEIN_VISION_URL)
    payload = {
        'sub': subject,
        'aud': url,
        'exp': expiry
    }

    try:
        return jwt.encode(payload, private_key, algorithm='RS256')
    except Exception as e:
        raise e

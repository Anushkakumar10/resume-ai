import jwt
from flask_jwt_extended import decode_token


def decode_jwt_token(token):
    """Decodes the JWT token and returns the payload."""
    try:
        payload = decode_token(token)
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

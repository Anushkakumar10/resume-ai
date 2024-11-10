# app/services/auth_service.py
# Provides authentication-related services.

from flask_jwt_extended import create_access_token


def generate_token(username):
    token = create_access_token(identity=username)
    return token

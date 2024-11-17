# app/services/auth_service.py
# Provides authentication-related services.

from datetime import timedelta

from flask_jwt_extended import create_access_token, get_jwt_identity
from werkzeug.security import check_password_hash

from app.models.user import User


def generate_token(user):
    """
    Generates a JWT token for the authenticated user.
    The token will be valid for 30 days by default.
    """
    access_token = create_access_token(identity=user.id, fresh=True, expires_delta=timedelta(days=7))
    return access_token


def validate_user_credentials(username, password):
    """Validate user credentials by checking username and password"""
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return user
    return None


def get_user_id_from_token():
    """Extract user from JWT token"""
    print("hello")
    user_id = get_jwt_identity()
    print(user_id)
    return user_id

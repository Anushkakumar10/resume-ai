# app/controllers/auth_controller.py
# Implements business logic related to authentication.

from flask import jsonify
from werkzeug.security import generate_password_hash

from ..extensions import db
from ..models.user import User
from ..services.auth_service import generate_token, validate_user_credentials


def signup_user(data):
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 409

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 409

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User signed up successfully"}), 201


def login_user(data):
    username = data.get('username')
    password = data.get('password')

    user = validate_user_credentials(username, password)
    if user:
        access_token = generate_token(user)
        return jsonify({"access_token": access_token}), 200
    return jsonify({"message": "Invalid credentials"}), 401

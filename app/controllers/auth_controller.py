# app/controllers/auth_controller.py
# Implements the business logic for authentication.

from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from ..extensions import db
from ..models.user import User
from ..services.auth_service import generate_token


def signup_user(data):
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 409

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User signed up successfully"}), 201


def login_user(data):
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid username or password"}), 401

    token = generate_token(user.username)
    return jsonify({"token": token}), 200

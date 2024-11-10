# app/routes/auth/user.py
# Defines authentication routes.


from flask import Blueprint, request

from ..controllers.auth_controller import signup_user, login_user

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    return signup_user(data)


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return login_user(data)

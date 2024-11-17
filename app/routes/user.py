# app/routes/user.py
# Defines user-related routes.

from flask import Blueprint, request

from ..controllers.user_controller import get_user_profile, update_user_profile

user_bp = Blueprint('user', __name__)


# Route to fetch user profile
@user_bp.route('/profile', methods=['GET'])
def profile():
    return get_user_profile()


# Route to update user profile
@user_bp.route('/profile', methods=['PUT'])
def update_profile():
    data = request.get_json()
    return update_user_profile(data)

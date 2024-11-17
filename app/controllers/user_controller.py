# app/controllers/user_controllers.py
# Implements business logic related to user actions.

from flask import jsonify
from flask_jwt_extended import jwt_required

from app.services.auth_service import get_user_id_from_token
from ..extensions import db
from ..models.user import User
from ..services.user_service import fetch_user


# Fetch user profile
@jwt_required()
def get_user_profile():
    user_id = get_user_id_from_token()
    if not user_id:
        return jsonify({'message': 'No token'}), 401

    user = fetch_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Serialize the user data
    user_data = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "phone": user.phone,
        "bio": user.bio,
        "profile_picture": user.profile_picture,
        "experiences": user.experiences,
        "educations": user.educations,
        "skills": user.skills,
        "certifications": user.certifications
    }
    return jsonify(user_data), 200


# Update user profile
@jwt_required()
def update_user_profile(data):
    user_id = get_user_id_from_token()
    if not user_id:
        return jsonify({'message': 'No token'}), 401

    user = fetch_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Update user fields if they exist in the request data
    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.phone = data.get('phone', user.phone)
    user.bio = data.get('bio', user.bio)
    user.profile_picture = data.get('profile_picture', user.profile_picture)

    # Update JSON fields
    user.experiences = data.get('experiences', user.experiences)
    user.educations = data.get('educations', user.educations)
    user.skills = data.get('skills', user.skills)
    user.certifications = data.get('certifications', user.certifications)

    try:
        db.session.commit()
        return jsonify({"message": "Profile updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

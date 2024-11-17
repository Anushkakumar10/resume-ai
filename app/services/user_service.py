# app/services/user_service.py
# Provides user-related services.

from ..extensions import db
from ..models.user import User


# Service to fetch user data
def fetch_user(user_id):
    return User.query.get(user_id)


# Service to update user data
def update_user(user, data):
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
        return {"message": "Profile updated successfully"}
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Failed to update profile: {str(e)}")

# app/models/user.py
# Defines the User model, representing user data stored in the database.

from ..extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(15), nullable=True)
    bio = db.Column(db.Text, nullable=True)

    # URL for profile picture
    profile_picture = db.Column(db.String(200), nullable=True)

    # JSON fields for flexible data storage
    experiences = db.Column(db.JSON, nullable=True)
    educations = db.Column(db.JSON, nullable=True)
    skills = db.Column(db.JSON, nullable=True)
    certifications = db.Column(db.JSON, nullable=True)

    def __repr__(self):
        return f'<User {self.username}>'

# app/config.py
# Contains configuration settings.

class Config:
    SECRET_KEY = 'refE6SRH0V6XFtSXIYhTa3lJEKc01dMV'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///resumeai.db'
    JWT_SECRET_KEY = 'uJJcOFnKNCvJTu3QuJ7RAf2Rpg4u0luR'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

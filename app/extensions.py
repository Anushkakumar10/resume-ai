# app/extensions.py
# Sets up extensions to be used across the app.

from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

jwt = JWTManager()
migrate = Migrate()
db = SQLAlchemy()

# app/__init__.py
# Initializes the Flask app and sets up the database, JWT, and routes.

from flask import Flask

from .config import Config
from .extensions import db, jwt, migrate
from .routes import init_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)


    # Initialize routes
    init_routes(app)

    with app.app_context():
        db.create_all()  # Creates the database tables if they don't exist

    return app

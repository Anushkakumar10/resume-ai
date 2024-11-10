# app/routes/__init__.py
# Initializes routes by registering each Blueprint with the main Flask app.

from .auth import auth_bp


def init_routes(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')

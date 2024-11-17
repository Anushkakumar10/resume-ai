# app/routes/__init__.py
# Initializes routes by registering each Blueprint with the main Flask app.

from .auth import auth_bp
from .cover_letter import cover_letter_bp
from .resume import resume_bp
from .template import template_bp
from .user import user_bp


def init_routes(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(cover_letter_bp, url_prefix='/cover_letter')
    app.register_blueprint(resume_bp, url_prefix='/resume')
    app.register_blueprint(template_bp, url_prefix='/templates')
    app.register_blueprint(user_bp, url_prefix='/user')

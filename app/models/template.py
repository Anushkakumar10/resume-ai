# app/models/template.py
# Defines the Template model for storing resume and cover letter templates.

from ..extensions import db


class Template(db.Model):
    __tablename__ = 'templates'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    type = db.Column(db.String(50), nullable=False)  # 'resume' or 'cover_letter'
    content = db.Column(db.Text, nullable=False)  # Template HTML content
    description = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return f"<Template {self.name} ({self.type})>"

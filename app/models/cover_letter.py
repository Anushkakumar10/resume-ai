# app/models/cover_letter.py
# Model representing user-created cover letters.

from sqlalchemy.dialects.postgresql import JSON

from ..extensions import db


class CoverLetter(db.Model):
    __tablename__ = 'cover_letters'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(150), nullable=False)
    company = db.Column(db.String(150), nullable=False)
    job_description = db.Column(db.Text, nullable=True)
    data = db.Column(JSON, nullable=False)  # JSON structure to hold cover letter content
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return f'<CoverLetter {self.title}>'

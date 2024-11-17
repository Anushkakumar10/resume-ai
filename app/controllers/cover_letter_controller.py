# app/controllers/cover_letter_controller.py
# Implements business logic related to cover letter actions.

from flask import jsonify
from flask_jwt_extended import jwt_required

from app.services.auth_service import get_user_id_from_token
from ..extensions import db
from ..models.cover_letter import CoverLetter


@jwt_required()
def create_cover_letter(req):
    user_id = get_user_id_from_token()
    if not user_id:
        return jsonify({'message': 'No token'}), 401

    data = req.get_json()
    title = data.get('title')
    role = data.get('role')
    company = data.get('company')
    job_description = data.get('job_description')
    cover_letter_data = data.get('data')  # Actual letter content

    if not title or not role or not company or not cover_letter_data:
        return jsonify({"error": "Title, role, company, and data are required"}), 400

    cover_letter = CoverLetter(
        title=title,
        user_id=user_id,
        role=role,
        company=company,
        job_description=job_description,
        data=cover_letter_data,
    )
    db.session.add(cover_letter)
    db.session.commit()

    return jsonify({"message": "Cover letter created successfully", "cover_letter": cover_letter.id}), 201


@jwt_required()
def get_user_cover_letters():
    user_id = get_user_id_from_token()
    if not user_id:
        return jsonify({'message': 'No token'}), 401

    cover_letters = CoverLetter.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": c.id, "title": c.title} for c in cover_letters]), 200


@jwt_required()
def get_cover_letter(cover_letter_id):
    cover_letter = CoverLetter.query.get_or_404(cover_letter_id)
    return jsonify({"id": cover_letter.id, "title": cover_letter.title, "data": cover_letter.data}), 200


@jwt_required()
def delete_cover_letter(cover_letter_id):
    cover_letter = CoverLetter.query.get_or_404(cover_letter_id)
    db.session.delete(cover_letter)
    db.session.commit()
    return jsonify({"message": "Cover letter deleted successfully"}), 200

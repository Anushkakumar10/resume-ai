# app/controllers/resume_controller.py
# Implements business logic related to resume actions.

from flask import jsonify
from flask_jwt_extended import jwt_required

from ..extensions import db
from ..models.resume import Resume
from app.services.auth_service import get_user_id_from_token


@jwt_required()
def create_resume(req):
    user_id = get_user_id_from_token()
    if not user_id:
        return jsonify({'message': 'No token'}), 401

    data = req.get_json()
    title = data.get('title')
    resume_data = data.get('data')

    if not title or not resume_data:
        return jsonify({"error": "Title and data are required"}), 400

    resume = Resume(title=title, user_id=user_id, data=resume_data)
    db.session.add(resume)
    db.session.commit()

    return jsonify({"message": "Resume created successfully", "resume": resume.id}), 201


@jwt_required()
def get_user_resumes():
    user_id = get_user_id_from_token()
    if not user_id:
        return jsonify({'message': 'No token'}), 401

    resumes = Resume.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": r.id, "title": r.title} for r in resumes]), 200


@jwt_required()
def get_resume(resume_id):
    resume = Resume.query.get_or_404(resume_id)
    return jsonify({"id": resume.id, "title": resume.title, "data": resume.data}), 200


@jwt_required()
def delete_resume(resume_id):
    resume = Resume.query.get_or_404(resume_id)
    db.session.delete(resume)
    db.session.commit()
    return jsonify({"message": "Resume deleted successfully"}), 200

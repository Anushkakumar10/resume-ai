# app/routes/resume.py
# Routes for managing resumes.

from flask import Blueprint, request

from ..controllers.resume_controller import create_resume, get_user_resumes, get_resume, delete_resume

resume_bp = Blueprint('resume', __name__)


@resume_bp.route('', methods=['POST'])
def create():
    return create_resume(request)


@resume_bp.route('', methods=['GET'])
def get_all():
    return get_user_resumes()


@resume_bp.route('/<int:resume_id>', methods=['GET'])
def get(resume_id):
    return get_resume(resume_id)


@resume_bp.route('/<int:resume_id>', methods=['DELETE'])
def delete(resume_id):
    return delete_resume(resume_id)

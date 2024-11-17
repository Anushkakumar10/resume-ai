# app/routes/cover_letter.py
# Routes for managing cover letters.

from flask import Blueprint, request

from ..controllers.cover_letter_controller import create_cover_letter, get_user_cover_letters, get_cover_letter, \
    delete_cover_letter

cover_letter_bp = Blueprint('cover_letter', __name__)


@cover_letter_bp.route('', methods=['POST'])
def create():
    return create_cover_letter(request)


@cover_letter_bp.route('', methods=['GET'])
def get_all():
    return get_user_cover_letters()


@cover_letter_bp.route('/<int:cover_letter_id>', methods=['GET'])
def get(cover_letter_id):
    return get_cover_letter(cover_letter_id)


@cover_letter_bp.route('/<int:cover_letter_id>', methods=['DELETE'])
def delete(cover_letter_id):
    return delete_cover_letter(cover_letter_id)

# app/routes/template.py
# Defines API routes for managing templates.

from flask import Blueprint, request

from ..controllers.template_controller import (
    get_all_templates,
    get_template_by_id,
    create_template,
    update_template,
    delete_template
)

template_bp = Blueprint('template', __name__)


# Route to fetch all templates
@template_bp.route('', methods=['GET'])
def all_templates():
    return get_all_templates()


# Route to fetch a specific template by ID
@template_bp.route('/<int:template_id>', methods=['GET'])
def template_by_id(template_id):
    return get_template_by_id(template_id)


# Route to create a new template
@template_bp.route('', methods=['POST'])
def create_new_template():
    data = request.get_json()
    return create_template(data)


# Route to update a template
@template_bp.route('/<int:template_id>', methods=['PUT'])
def update_existing_template(template_id):
    data = request.get_json()
    return update_template(template_id, data)


# Route to delete a template
@template_bp.route('/<int:template_id>', methods=['DELETE'])
def delete_existing_template(template_id):
    return delete_template(template_id)

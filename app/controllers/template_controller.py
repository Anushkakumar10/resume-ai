# app/controllers/template_controller.py
# Implements business logic related to template actions.

from flask import jsonify, request
from flask_jwt_extended import jwt_required

from ..extensions import db
from ..models.template import Template


@jwt_required()
def get_all_templates():
    """Fetch all available templates."""
    templates = Template.query.all()
    return jsonify([{
        "id": template.id,
        "name": template.name,
        "type": template.type,
        "description": template.description,
        "created_at": template.created_at,
        "updated_at": template.updated_at
    } for template in templates])


@jwt_required()
def get_template_by_id(template_id):
    """Fetch a specific template by ID."""
    template = Template.query.get(template_id)
    if not template:
        return jsonify({"error": "Template not found"}), 404

    return jsonify({
        "id": template.id,
        "name": template.name,
        "type": template.type,
        "content": template.content,
        "description": template.description,
        "created_at": template.created_at,
        "updated_at": template.updated_at
    })


@jwt_required()
def create_template():
    """Create a new template."""
    data = request.json
    try:
        new_template = Template(
            name=data['name'],
            type=data['type'],
            content=data['content'],
            description=data.get('description')
        )
        db.session.add(new_template)
        db.session.commit()
        return jsonify({"message": "Template created successfully", "id": new_template.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@jwt_required()
def update_template(template_id):
    """Update an existing template."""
    data = request.json
    template = Template.query.get(template_id)
    if not template:
        return jsonify({"error": "Template not found"}), 404

    try:
        template.name = data.get('name', template.name)
        template.type = data.get('type', template.type)
        template.content = data.get('content', template.content)
        template.description = data.get('description', template.description)
        db.session.commit()
        return jsonify({"message": "Template updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@jwt_required()
def delete_template(template_id):
    """Delete a template."""
    template = Template.query.get(template_id)
    if not template:
        return jsonify({"error": "Template not found"}), 404

    try:
        db.session.delete(template)
        db.session.commit()
        return jsonify({"message": "Template deleted successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

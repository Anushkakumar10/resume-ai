# app/services/template_service.py
# Provides reusable template-related business logic.

from ..models.template import Template


def get_templates_by_type(template_type):
    """Fetch templates by type ('resume', 'cover_letter')."""
    return Template.query.filter_by(type=template_type).all()


def search_templates(keyword):
    """Search templates by keyword in name or description."""
    return Template.query.filter(
        Template.name.ilike(f"%{keyword}%") |
        Template.description.ilike(f"%{keyword}%")
    ).all()

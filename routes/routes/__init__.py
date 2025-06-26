from flask import Blueprint
from .routes.analytics import analytics_bp
from .routes.routes.pharmacy import pharmacy_bp
from .routes.routes.routes.reports import reports_bp

__all__ = ["register_blueprints"]

def register_blueprints(app):
    app.register_blueprint(analytics_bp)
    app.register_blueprint(pharmacy_bp)
    app.register_blueprint(reports_bp)

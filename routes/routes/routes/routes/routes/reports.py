from flask import Blueprint, jsonify
from db import get_connection

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/unpaid-orders')
def unpaid_orders():
    # unpaid orders SQL here
    ...

@reports_bp.route('/top-customers')
def top_customers():
    # top customers SQL here
    ...

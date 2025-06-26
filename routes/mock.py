from flask import Blueprint, jsonify

mock_bp = Blueprint('mock', __name__)

@mock_bp.route('/monthly-sales')
def monthly_sales():
    # Return mock monthly sales data
    return jsonify([
        {"month": "2025-01", "monthly_sales": 1200},
        {"month": "2025-02", "monthly_sales": 950},
        {"month": "2025-03", "monthly_sales": 1500},
        {"month": "2025-04", "monthly_sales": 1100},
        {"month": "2025-05", "monthly_sales": 900}
    ])

@mock_bp.route('/pharmacy/<int:pharmacy_id>/summary')
def pharmacy_summary(pharmacy_id):
    # Return mock summary for any pharmacy
    return jsonify({
        "pharmacy_name": f"Pharmacy #{pharmacy_id}",
        "total_orders": 12 + pharmacy_id,
        "total_spent": 1000 * pharmacy_id,
        "last_order_date": "2025-05-15"
    })

@mock_bp.route('/pharmacy/<int:pharmacy_id>/top-products')
def top_products(pharmacy_id):
    # Return mock top products
    return jsonify([
        {"product_name": "Paracetamol 500mg", "times_ordered": 10},
        {"product_name": "Ibuprofen 200mg", "times_ordered": 7},
        {"product_name": "Cough Syrup", "times_ordered": 5}
    ])

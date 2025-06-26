from flask import Blueprint, jsonify
from db import get_connection

pharmacy_bp = Blueprint('pharmacy', __name__)

@pharmacy_bp.route('/pharmacy/<int:pharmacy_id>/summary')
def pharmacy_summary(pharmacy_id):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute('''
        SELECT p.name AS pharmacy_name,
               COUNT(o.id) AS total_orders,
               COALESCE(SUM(o.total), 0) AS total_spent,
               MAX(o.order_date) AS last_order_date
        FROM pharmacies p
        LEFT JOIN orders o ON o.pharmacy_id = p.id
        WHERE p.id = %s
        GROUP BY p.id
    ''', (pharmacy_id,))
    data = cur.fetchone()
    cur.close()
    conn.close()
    if not data:
        return jsonify({'error': 'Pharmacy not found'}), 404
    return jsonify(data)

@pharmacy_bp.route('/pharmacy/<int:pharmacy_id>/top-products')
def top_products(pharmacy_id):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute('''
        SELECT pr.name AS product_name, SUM(oi.quantity) AS times_ordered
        FROM orders o
        JOIN order_items oi ON oi.order_id = o.id
        JOIN products pr ON pr.id = oi.product_id
        WHERE o.pharmacy_id = %s
        GROUP BY pr.id
        ORDER BY times_ordered DESC
        LIMIT 5
    ''', (pharmacy_id,))
    data = cur.fetchall()
    cur.close()
    conn.close()
    if not data:
        return jsonify({'message': 'No products found for this pharmacy.'})
    return jsonify(data)

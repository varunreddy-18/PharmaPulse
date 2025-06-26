from flask import Blueprint, jsonify
from db import get_connection

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/monthly-sales')
def monthly_sales():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute('''
        SELECT DATE_FORMAT(order_date, '%Y-%m') AS month, SUM(total) AS monthly_sales
        FROM orders
        GROUP BY month
        ORDER BY month
    ''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

@analytics_bp.route('/debug/pharmacies')
def debug_pharmacies():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute('SELECT * FROM customers')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

@analytics_bp.route('/debug/orders')
def debug_orders():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute('SELECT * FROM orders')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

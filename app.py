from flask import Flask, jsonify, render_template
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Varun@9154',
    'database': 'med_agency'
}

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to Med Agency API'})

@app.route('/pharmacy/<int:pharmacy_id>/monthly-sales')
def pharmacy_monthly_sales(pharmacy_id):
    conn = mysql.connector.connect(**db_config)
    cur = conn.cursor(dictionary=True)
    cur.execute('''
        SELECT DATE_FORMAT(order_date, '%Y-%m') AS month, SUM(total_amount) AS monthly_sales
        FROM orders
        WHERE customer_id = %s
        GROUP BY month
        ORDER BY month
    ''', (pharmacy_id,))
    data = cur.fetchall()
    cur.close()
    conn.close()
    # If no sales, return zero sales for the last 6 months
    if not data:
        from datetime import datetime, timedelta
        today = datetime.today()
        months = [(today.replace(day=1) - timedelta(days=30*i)).strftime('%Y-%m') for i in range(5, -1, -1)]
        data = [{"month": m, "monthly_sales": 0} for m in months]
    return jsonify(data)

@app.route('/monthly-sales')
def monthly_sales():
    conn = mysql.connector.connect(**db_config)
    cur = conn.cursor(dictionary=True)
    cur.execute('''
        SELECT DATE_FORMAT(order_date, '%Y-%m') AS month, SUM(total_amount) AS monthly_sales
        FROM orders
        GROUP BY month
        ORDER BY month
    ''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

@app.route('/pharmacy/<int:pharmacy_id>/summary')
def pharmacy_summary(pharmacy_id):
    conn = mysql.connector.connect(**db_config)
    cur = conn.cursor(dictionary=True)
    cur.execute('''
        SELECT name FROM customers WHERE customer_id = %s
    ''', (pharmacy_id,))
    row = cur.fetchone()
    if not row:
        cur.close()
        conn.close()
        return jsonify({'error': 'Pharmacy not found'}), 404
    cur.close()
    conn.close()
    return jsonify({
        "pharmacy_name": row['name'],
        "total_orders": 12 + pharmacy_id,  # Replace with real query if needed
        "total_spent": 1000 * pharmacy_id, # Replace with real query if needed
        "last_order_date": "2025-05-15"   # Replace with real query if needed
    })

@app.route('/pharmacy/<int:pharmacy_id>/top-products')
def top_products(pharmacy_id):
    # You can implement a real query here if you have order_items/products tables
    return jsonify([
        {"product_name": "Paracetamol 500mg", "times_ordered": 10},
        {"product_name": "Ibuprofen 200mg", "times_ordered": 7},
        {"product_name": "Cough Syrup", "times_ordered": 5}
    ])

if __name__ == '__main__':
    app.run(debug=True)

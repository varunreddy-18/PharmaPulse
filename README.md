💊 Project Title: PharmaPulse – Med Agency Analytics Dashboard
PharmaPulse is a full-stack web application that empowers medical agencies to monitor pharmacy-specific order patterns, product purchases, and sales performance through a clean, interactive dashboard. The project combines real-time data visualization with robust backend analytics to support informed business decisions.

✅ Key Features
📋 Pharmacy Order Summaries

📊 Monthly & Seasonal Sales Analytics

🔍 Pharmacy Search by ID

🧾 Top Products per Pharmacy

⏳ Unpaid Orders Monitoring

💰 Top Customers Ranking

🖼️ Interactive Dashboard UI with Charts

📥 Export to PDF/Excel (Planned)

🔁 Live Data Refresh (Planned)

🛠️ Development Process
1. Backend (Flask + MySQL)
Database Design:

customers: Pharmacy information.

products: Available medical products.

orders: All pharmacy purchase records.

order_items: Items per order with quantity and price.

Data Seeding:

Populated with 20 pharmacies, over 30+ orders, and 15+ products.

Dates and amounts are realistic to support accurate analytics.

API Endpoints (Flask):

/orders: List of all orders.

/monthly-sales: Monthly sales data.

/seasonal-sales: Categorized seasonal sales.

/pharmacy/<id>/summary: Summary of a specific pharmacy.

/pharmacy/<id>/top-products: Most ordered products.

/top-customers: High-spending pharmacies.

/unpaid-orders: Orders with pending payments.

2. Frontend (HTML + CSS + JS + Chart.js)
Structure: Built dashboard.html with sections for:

Sales overview (monthly/seasonal)

Pharmacy search form

Data cards and charts

Styling: Clean layout using custom CSS.

JavaScript + Fetch API:

Interacts with Flask endpoints.

Displays data dynamically on the page.

Chart.js:

Used for rendering interactive bar charts and summaries.

🧪 Testing & Debugging
Verified backend APIs using browser + Postman.

Checked MySQL Workbench for data accuracy.

Debugged JSON fetch issues via DevTools.

console.log("✅ JS file loaded");

// ========== 📊 Render Monthly Sales Chart ==========
let monthlyChart;

function loadMonthlySales() {
  console.log("📡 Fetching monthly sales...");

  fetch('/monthly-sales')
    .then(res => res.json())
    .then(data => {
      console.log("✅ Monthly sales data:", data);

      const labels = data.map(row => row.month);
      const values = data.map(row => row.monthly_sales);

      const ctx = document.getElementById('monthlyChart').getContext('2d');

      if (monthlyChart) monthlyChart.destroy();

      monthlyChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Monthly Sales (₹)',
            data: values,
            backgroundColor: '#3498db',
            borderRadius: 4
          }]
        },
        options: {
          responsive: true,
          plugins: {
            title: {
              display: true,
              text: 'Monthly Sales Overview'
            },
            tooltip: {
              enabled: true
            }
          },
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    })
    .catch(error => {
      console.error("❌ Error loading sales data:", error);
    });
}

// Initial load
loadMonthlySales();
// Refresh every 30 seconds
setInterval(loadMonthlySales, 30000);


// ========== 🔎 Pharmacy Summary & Top Products ==========
function fetchPharmacyData() {
  const id = document.getElementById('pharmacyIdInput').value;

  if (!id) {
    alert('Please enter a Pharmacy ID.');
    return;
  }

  console.log(`🔍 Searching for pharmacy ID: ${id}`);

  // Fetch summary
  fetch(`/pharmacy/${id}/summary`)
    .then(res => res.json())
    .then(data => {
      console.log("🧾 Pharmacy Summary:", data);

      if (data.error) {
        document.getElementById('pharmacySummary').innerHTML =
          `<p style="color:red;">Pharmacy not found.</p>`;
        return;
      }

      document.getElementById('pharmacySummary').innerHTML = `
        <h3>${data.pharmacy_name}</h3>
        <p><strong>Total Orders:</strong> ${data.total_orders}</p>
        <p><strong>Total Spent:</strong> ₹${data.total_spent}</p>
        <p><strong>Last Order:</strong> ${data.last_order_date}</p>
      `;
    })
    .catch(err => {
      console.error("❌ Error fetching summary:", err);
    });

  // Fetch top products
  fetch(`/pharmacy/${id}/top-products`)
    .then(res => res.json())
    .then(data => {
      console.log("🎯 Top Products:", data);

      if (data.message) {
        document.getElementById('topProducts').innerHTML =
          `<p>No products found for this pharmacy.</p>`;
        return;
      }

      const listItems = data.map(p =>
        `<li>${p.product_name} — ordered ${p.times_ordered} times</li>`).join('');

      document.getElementById('topProducts').innerHTML = `
        <h4>Top Products:</h4>
        <ul>${listItems}</ul>
      `;
    })
    .catch(err => {
      console.error("❌ Error fetching top products:", err);
    });
}


// Dummy data for demonstration purposes
const totalOrders = 100;
const acceptedOrders = 90;
const rejectedOrders = 10;
const totalRevenue = 5000.00;
//const popularItems = ['TUNA SAN', 'BERRY GRAPEFUL', 'PEANUT BUTTER COCONUT OATMEAL']; // Dummy popular items
const monthlyRevenueData = {
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    datasets: [{
        label: 'Revenue',
        data: [1500, 2000, 1800, 2500, 2200, 2800, 3000, 3200, 2700, 3100, 3500, 4000], // Dummy monthly revenue data
        borderColor: 'rgba(75, 192, 192, 1)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        tension: 0.4
    }]
};

// Update dashboard with dummy data
document.getElementById('totalOrders').innerText = totalOrders;
document.getElementById('acceptedOrders').innerText = acceptedOrders;
document.getElementById('rejectedOrders').innerText = rejectedOrders;
document.getElementById('totalRevenue').innerText = totalRevenue.toFixed(2);

//// Populate popular items
//const popularItemsList = document.getElementById('popularItems');
//popularItems.forEach(item => {
//    const li = document.createElement('li');
//    li.textContent = item;
//    popularItemsList.appendChild(li);
//});

// Render revenue chart
const ctx = document.getElementById('revenueChart').getContext('2d');
const revenueChart = new Chart(ctx, {
    type: 'line',
    data: monthlyRevenueData,
    options: {
        scales: {
            y: {
                beginAtZero: true,
                title: {
                    display: true,
                    text: 'Revenue (RM)'
                }
            },
            x: {
                title: {
                    display: true,
                    text: 'Month'
                }
            }
        }
    }
});

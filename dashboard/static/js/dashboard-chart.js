document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('revenueChart').getContext('2d');
    const weeks = JSON.parse('{{ weeks|escapejs }}');
    const revenues = JSON.parse('{{ revenues|escapejs }}');

    const weeklyRevenueData = {
        labels: weeks,
        datasets: [{
            label: 'Revenue',
            data: revenues,
            borderColor: 'rgba(75, 192, 192, 1)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            tension: 0.4
        }]
    };

    const revenueChart = new Chart(ctx, {
        type: 'line',
        data: weeklyRevenueData,
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
                        text: 'Week'
                    }
                }
            }
        }
    });
});

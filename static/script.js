// Theme toggle
function toggleTheme() {
    const html = document.documentElement;
    const button = document.querySelector('.theme-toggle');
    const currentTheme = html.getAttribute("data-theme");
    const newTheme = currentTheme === "light" ? "dark" : "light";
    html.setAttribute("data-theme", newTheme);
    button.textContent = newTheme === "dark" ? "☀️" : "🌙";
}

// Format number to Indian currency style (e.g., ₹12,34,567)
function formatCurrency(num) {
    return '₹' + Number(num).toLocaleString('en-IN');
}

// Convert number to human-readable (e.g., 1.2 Cr, 56.4 Lakh)
function toReadableAmount(value) {
    value = Number(value);
    if (value >= 10000000) {
        return (value / 10000000).toFixed(1) + ' Cr';
    } else if (value >= 100000) {
        return (value / 100000).toFixed(1) + ' Lakh';
    } else {
        return formatCurrency(value);
    }
}

// Donut chart rendering (for investment calculator)
function renderDonutChart(invested, returns, canvasId = 'sipChart') {
    const ctx = document.getElementById(canvasId);
    if (!ctx) return;

    if (window.myChart) {
        window.myChart.destroy(); // destroy previous if exists
    }

    window.myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Invested Amount', 'Estimated Returns'],
            datasets: [{
                data: [invested, returns],
                backgroundColor: ['#28a745', '#ffc107'],
                borderWidth: 1
            }]
        },
        options: {
            cutout: '70%',
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });
}

// Update live output on slider move
function setupLiveSliders(sliderId, outputId, prefix = '', suffix = '') {
    const slider = document.getElementById(sliderId);
    const output = document.getElementById(outputId);
    if (slider && output) {
        output.textContent = prefix + slider.value + suffix;
        slider.addEventListener('input', () => {
            output.textContent = prefix + slider.value + suffix;
        });
    }
}

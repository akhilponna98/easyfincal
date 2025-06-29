// ------------------------------
// Theme toggle logic with persistence
// ------------------------------
function toggleTheme() {
  const html = document.documentElement;
  const button = document.querySelector('.theme-toggle');
  const currentTheme = html.getAttribute("data-theme");
  const newTheme = currentTheme === "light" ? "dark" : "light";
  html.setAttribute("data-theme", newTheme);
  if (button) button.textContent = newTheme === "dark" ? "☀️" : "🌙";
  localStorage.setItem('theme', newTheme); // Save preference
}

// On page load, set theme from localStorage if available
document.addEventListener("DOMContentLoaded", () => {
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    document.documentElement.setAttribute("data-theme", savedTheme);
    const button = document.querySelector('.theme-toggle');
    if (button) button.textContent = savedTheme === "dark" ? "☀️" : "🌙";
  }
});

// ------------------------------
// Format number: Indian style ₹
// ------------------------------
function formatCurrency(num) {
  return '₹' + Number(num).toLocaleString('en-IN');
}

// ------------------------------
// Human-readable: Cr / Lakh
// ------------------------------
function toReadableAmount(value) {
  value = Number(value);
  if (value >= 1e7) {
    return (value / 1e7).toFixed(1) + ' Cr';
  } else if (value >= 1e5) {
    return (value / 1e5).toFixed(1) + ' Lakhs';
  } else {
    return formatCurrency(value);
  }
}

// ------------------------------
// Donut Chart for SIP break-up
// (supports multiple charts on one page, compact aspect ratio)
// ------------------------------
window.charts = window.charts || {};
function renderDonutChart(invested, returns, canvasId = 'sipDonutChart') {
  const ctx = document.getElementById(canvasId);
  if (!ctx) return;

  // Destroy existing chart on this canvas if present
  if (window.charts[canvasId]) {
    window.charts[canvasId].destroy();
  }

  window.charts[canvasId] = new Chart(ctx, {
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
      aspectRatio: 1, // Compact, square chart
      maintainAspectRatio: true,
      cutout: '70%',
      plugins: {
        legend: {
          position: 'bottom'
        }
      }
    }
  });
}

// ------------------------------
// Example: live slider (optional)
// ------------------------------
// This is for reuse in other calculators if needed.
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

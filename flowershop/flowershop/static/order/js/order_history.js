
document.addEventListener("DOMContentLoaded", function() {
  const statusElements = document.querySelectorAll(".order-status");

  statusElements.forEach(function(statusElement) {
    const circle = statusElement.nextElementSibling;
    const status = statusElement.textContent.trim();

    if (!circle) return;

    if (status === "W oczekiwaniu") {
      circle.style.backgroundColor = "#f39c12";
    } else if (status === "W dostawie") {
      circle.style.backgroundColor = "#27ae60";
    } else if (status === "Dostarczone") {
      circle.style.backgroundColor = "#2ecc71";
    } else if (status === "Anulowane") {
      circle.style.backgroundColor = "#e74c3c";
    }
  });
});

document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById("toggleButton");
    const profileData = document.getElementById("profileData");
    const profileEdit = document.getElementById("profileEdit");
  
    toggleButton.addEventListener("click", function() {
      
      if (profileData.style.display === "none") {
        profileData.style.display = "block";
        profileEdit.style.display = "none";
        toggleButton.textContent = "Edytuj";
      } else {
        profileData.style.display = "none";
        profileEdit.style.display = "block";
        toggleButton.textContent = "Wróc";
      }
    });
  
    // Obsługa formularza
    const editForm = document.getElementById("editForm");
    editForm.addEventListener("submit", function(event) {
      profileData.style.display = "block";
      profileEdit.style.display = "none";
      toggleButton.textContent = "Edytuj";
    });
  });
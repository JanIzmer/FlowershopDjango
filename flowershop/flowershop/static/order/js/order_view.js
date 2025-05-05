function goToStep(step) {
    const steps = document.querySelectorAll('.step');
    const labels = document.querySelectorAll('.step-label');
    const progressBar = document.getElementById('progress-bar');
  
    steps.forEach((el, index) => {
      el.style.display = index === (step - 1) ? 'block' : 'none';
    });
  
    labels.forEach((label, index) => {
      label.classList.toggle('active', index === (step - 1));
    });
  
    const progressPercent = ((step - 1) / (steps.length - 1)) * 100;
    progressBar.style.width = `${progressPercent}%`;
  }
  
function initAutocomplete() {
    var input = document.getElementById('address');
    var autocomplete = new google.maps.places.Autocomplete(input);

   
    autocomplete.addListener('place_changed', function() {
        var place = autocomplete.getPlace();

        
        if (!place.geometry) {
            return;
        }

        
        document.getElementById('addressDetails').style.display = 'block';
        document.getElementById('street').value = place.address_components.find(component => component.types.includes("route"))?.long_name || '';
        document.getElementById('city').value = place.address_components.find(component => component.types.includes("locality"))?.long_name || '';
        document.getElementById('postal_code').value = place.address_components.find(component => component.types.includes("postal_code"))?.long_name || '';
        document.getElementById('country').value = place.address_components.find(component => component.types.includes("country"))?.long_name || '';
    });
}


function loadGoogleMaps() {
    var script = document.createElement('script');
    script.src = `https://maps.googleapis.com/maps/api/js?key=AIzaSyB3BcrMdWiIGS3h0dokNVk__yOkHvWRUhM&libraries=places&callback=initAutocomplete`;
    script.async = true;
    script.defer = true;
    document.head.appendChild(script);
}


window.onload = loadGoogleMaps;

  
  document.addEventListener('DOMContentLoaded', function() {
    goToStep(1);
  
    const radios = document.querySelectorAll('input[name="delivery_method"]');
    const courierFields = document.getElementById('courierFields');
    const pickupInfo = document.getElementById('pickupInfo');
  
    radios.forEach(radio => {
      radio.addEventListener('change', function() {
        if (this.value === 'courier') {
          courierFields.style.display = 'block';
          pickupInfo.style.display = 'none';
        } else if (this.value === 'pickup') {
          courierFields.style.display = 'none';
          pickupInfo.style.display = 'block';
        }
      });
    });
  });
 
  document.addEventListener('DOMContentLoaded', () => goToStep(1));
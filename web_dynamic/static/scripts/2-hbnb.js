document.addEventListener('DOMContentLoaded', function () {
  $.get('http://localhost:5001/api/v1/status/', function (data, status) {
    if (data.status === 'OK') {
      $('#api_status').addClass('available');
    } else {
      $('#api_status').removeClass('available');
    }
  });
});
document.addEventListener('DOMContentLoaded', function () {
  const amenities = {};
  $('input[type="checkbox"]').change(function () {
    if ($(this).is(':checked')) {
      amenities[$(this).data('id')] = $(this).data('name');
    } else {
      delete amenities[$(this).data('id')];
    }
    const amenitiesList = Object.values(amenities);
    if (amenitiesList.length > 0) {
      $('.amenities h4').text(amenitiesList.join(', '));
    } else {
      $('.amenities h4').html('&nbsp;');
    }
  }
  );
});

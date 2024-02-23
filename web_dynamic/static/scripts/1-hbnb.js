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

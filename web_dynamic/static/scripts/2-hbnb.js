$(document).ready(function () {
  const selectedAmenities = {};

  $.get('http://0.0.0.0:5001/api/v1/status/', function (data) {
    if (data.status === 'OK') {
      $('div#api_status').addClass('available');
    } else {
      $('div#api_status').removeClass('available');
    }
  });
  $('input[type="checkbox"]').change(function (data) {
    const amenity_id = $(this).data('id');
    const amenity_name = $(this).data('name');

    if (this.checked) {
      selectedAmenities[amenity_id] = amenity_name;
    } else {
      delete selectedAmenities[amenity_id];
    }

    $('.amenities h4').text(Object.values(selectedAmenities).join(', '));
  });
})

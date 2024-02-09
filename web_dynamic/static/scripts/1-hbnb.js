$(document).ready(function () {
  const selectedAmenities = {};

  $('input[type="checkbox"]').change(function (data) {
    const amenity_id = $(this).data('id');
    const amenity_name = $(this).data('name');

    if (this.checked) {
      selectedAmenities[amenity_id] = amenity_name;
    } else {
      delete selectedAmenities[amenity_id];
    }

    $('h4').text(Object.values(selectedAmenities).join(', '));
  });
})

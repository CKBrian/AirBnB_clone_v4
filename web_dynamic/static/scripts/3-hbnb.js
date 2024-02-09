$(document).ready(function () {
  const selectedAmenities = {};

  $.get('http://0.0.0.0:5001/api/v1/status/', function (data) {
    if (data.status === 'OK') {
      $('div#api_status').addClass('available');
    } else {
      $('div#api_status').removeClass('available');
    }
  });

  $.ajax({
    type: 'POST',
    url: 'http://0.0.0.0:5001/api/v1/places_search/',
    contentType: 'application/json',
    data: JSON.stringify({}),
    success: function(data) {
	for (const place of data) {
	    const article = `<article>
				<div class="title_box">
				    <h2>${place.name}</h2>
				    <div class="price_by_night">${place.price_by_night}</div>
				</div>
				<div class="information">
				    <div class="max_guest">${place.max_guest} Guests</div>
				    <div class="number_rooms">${place.number_rooms} Bedrooms</div>
				    <div class="number_bathrooms">${place.number_bathrooms} Bathrooms</div>
				</div>
				<div class="description">${place.description}</div>
			    </article>`;
	    // Append the article tag to the section.places
	    $('section.places').append(article);
	}
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

    $('h4').text(Object.values(selectedAmenities).join(', '));
  });
})

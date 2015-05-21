function initialize() {
	var mapOptions = {
		zoom: 17,
		center: new google.maps.LatLng(-6.887312469295931,-38.557607531547546),
		mapTypeId: google.maps.MapTypeId.ROADMAP
	}

	var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);

	var input = document.getElementById('search-input');

	var marker = new google.maps.Marker({
		position: map.getCenter(),
		map: map
	});

	var autocomplete = new google.maps.places.Autocomplete(input);
	autocomplete.setTypes(['geocode']);
	autocomplete.bindTo('bounds', map);

	if(navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(function(position) {
			var pos = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
			map.setCenter(pos);
			setMarker(pos);
		}, function() {
			handleNoGeolocation(true);
		});
	} else {
		handleNoGeolocation(false);
	}


	google.maps.event.addListener(map, 'click', function(event) {
		setMarker(event.latLng);
	});

	function setMarker(location) {
		marker.setVisible(false);
		marker.setPosition(location);
		$('#latitude').val(location.lat());
		$('#longitude').val(location.lng());
		marker.setVisible(true);
	}

	function handleNoGeolocation(errorFlag) {
		if (errorFlag) {
			window.alert('Error: The Geolocation service failed.');
		} else {
			window.alert('Error: Your browser doesn\'t support geolocation.');
		}
	}

	google.maps.event.addListener(autocomplete, 'place_changed', function() {
		var place = autocomplete.getPlace();
		if (!place.geometry) {
			window.alert("Autocomplete's returned place contains no geometry");
			return;
		}
		if (place.geometry.viewport) {
			map.fitBounds(place.geometry.viewport);
		} else {
			map.setCenter(place.geometry.location);
		}
		setMarker(place.geometry.location);
	});

}

google.maps.event.addDomListener(window, 'load', initialize);
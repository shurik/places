$(function() {
  var browserSupportFlag;
  var latlng = new google.maps.LatLng(-34.397, 150.644);
  var map = new google.maps.Map($('#map')[0], {
    zoom: 8,
    center: latlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  });
  if(navigator.geolocation) {
    $.jGrowl("Locating...");
    browserSupportFlag = true;
    navigator.geolocation.getCurrentPosition(function(position) {
      initialLocation = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
      $.jGrowl("Found your location");
      map.setCenter(initialLocation);
    }, function() {
      $.jGrowl("Your browser doesn't support GeoLocation");
    });
  }
})
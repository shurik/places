$(function() {
  var latlng = new google.maps.LatLng(-34.397, 150.644);
  var map = new google.maps.Map($('#map')[0], {
    zoom: 8,
    center: latlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  });
})
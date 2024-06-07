const mapLink = document.getElementById("map-link");
console.log(mapLink);
var address = document.getElementById("event-location").innerHTML;
console.log({ address });

// Check if the device is a mobile device


console.log(mapLink);

const upcomingEventscontainer = document.getElementById("upcoming-events");
upcomingEventscontainer.addEventListener("click", function () {
  address = document.getElementById("event-location").innerHTML;
  console.log({addressAgain: address});
});

// document.getElementById('map-div').addEventListener('click', function() {
//     var address = document.getElementById('event-location').innerText;
//     var googleMapsAppUrl = 'comgooglemaps://?q=' + encodeURIComponent(address);
//     var googleMapsWebUrl = 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(address);

//     // Try to open the Google Maps app
//     window.location = googleMapsAppUrl;

//     // If the Maps app is not available, fallback to opening in a web browser after a short delay
//     setTimeout(function() {
//         window.open(googleMapsWebUrl, '_blank')
//     }, 500);
// });

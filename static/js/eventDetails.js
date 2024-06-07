$(document).ready(function () {
  let eventId;

  // Function to fetch and display event details
  function fetchEventDetails(eventSlug) {
    $.ajax({
      url: `/events/upcoming/${eventSlug}/`,
      type: "GET",
      success: function (data) {
        $("#event-theme").text(data.theme);
        $("#event-description").text(data.description);
        $("#event-time").text(data.time);
        $("#event-date").text(formatDate(data.date));
        $("#event-location").text(data.location);
        $("#event-image").attr("src", data.image_url);

        // Add to calendar
        $(".title").text(data.theme);
        $(".start").text(`${data.date} ${data.time}`);
        $(".location").text(data.location);

        handleLocationMap()

        eventId = data.id;

        $("#event-details").removeClass("hidden");
        scrollToEventDetail();
      },
      error: function (xhr, status, error) {
        console.error("Error", xhr.responseText);
      },
    });
  }

  // Check if there's an event pk in the URL on page load
  var urlParams = new URLSearchParams(window.location.search);
  if (urlParams.has("event")) {
    var eventPk = urlParams.get("event");
    fetchEventDetails(eventPk);
  }

  // Event listener for click events to show event details
  $(".show-event-detail").click(function () {
    var eventSlug = $(this).data("event-slug");
    fetchEventDetails(eventSlug);

    // Update the URL with the event pk
    var newUrl =
      window.location.protocol +
      "//" +
      window.location.host +
      window.location.pathname +
      "?event=" +
      eventSlug;
    window.history.pushState({ path: newUrl }, "", newUrl);
  });

  // Handle browser back/forward buttons
  window.onpopstate = function (event) {
    if (event.state && event.state.path) {
      console.log({ state: event.state });
      var eventSlug = new URL(event.state.path).searchParams.get("event");
      fetchEventDetails(eventSlug);
    }
  };

  $(document).on(
    "click",
    "[data-modal-target='event-registration-form']",
    function () {
      // Set the value of the hidden field to the event ID for event registration
      $("#event-id-input").val(eventId);
    }
  );
});

function scrollToEventDetail() {
  var eventDetailsOffset = $("#event-details").offset().top;
  $("html, body").animate(
    {
      scrollTop: eventDetailsOffset,
    },
    "slow"
  );
}

function formatDate(dateString) {
  const date = new Date(dateString);
  const options = { month: "long", day: "numeric", year: "numeric" };
  return date.toLocaleDateString("en-US", options);
}

function handleLocationMap() {
  const mapLink = document.getElementById("map-link");
  const address = document.getElementById("event-location").innerHTML;

  mapLink.href = `https://www.google.com/maps?q=${encodeURIComponent(
    address
  )}`;
}

$(document).ready(function () {
  let eventId;

  // Fetch and display event details
  function fetchEventDetails(eventSlug) {
    $.ajax({
      url: `/events/json/${eventSlug}/`,
      type: "GET",
      success: function (data) {
        $("#event-theme").text(data.theme);
        $("#event-description").text(data.description);
        $("#event-time").text(data.time);
        $("#event-date").text(formatDate(data.date));
        $("#event-location").text(data.location);
        $("#event-image").attr("src", data.image_url);
        $("#event-content").html(data.content);

        toggleEventActions(data);

        // Add to calendar
        $(".title").text(data.theme);
        $(".start").text(`${data.date} ${data.time}`);
        $(".location").text(data.location);

        handleLocationMap();

        eventId = data.id;

        $("#event-details").removeClass("hidden");
        scrollToEventDetail();
      },
      error: function (xhr, status, error) {
        console.error("Error", xhr.responseText);
      },
    });
  }

  if (window.location.pathname.split("/").length > 2) {
    // Extract event slug from path (handling trailing slash)
    var pathSegments = window.location.pathname.split("/");
    pathSegments.pop().trim(); // Remove trailing slash and whitespace
    const slug = pathSegments[pathSegments.length - 1];

    // Check for valid event slug (excluding "events" and empty string)
    if (slug !== "events" && slug !== "") {
      // Fetch event details based on slug
      fetchEventDetails(slug);
    }
  }

  // Event listener for click events to show event details
  $(".show-event-detail").click(function () {
    var eventSlug = $(this).data("event-slug");
    fetchEventDetails(eventSlug);

    var newUrl = window.location.origin + "/events/" + eventSlug;
    window.history.pushState({ path: newUrl }, "", newUrl);
  });

  // Handle browser back/forward buttons
  window.onpopstate = function (event) {
      var url = window.location.origin + window.location.pathname;
      
      const segments = url.split("/");
      if(segments.length === 6) {
        // There could an empty string at the end, we pop that off
        // so the slug is the last item
        segments.pop()
      }
      var lastIndex = segments[segments.length - 1];
      if (lastIndex !== "events" && lastIndex !== '') {
        // then last index is the slug
        fetchEventDetails(lastIndex);
      } else {
        $("#event-details").addClass('hidden');
      }
  };

  $(document).on(
    "click",
    "[data-modal-target='event-registration-form']",
    function () {
      // Set the value of the hidden event_id field, in the event registration
      // form to the event ID for event registration
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
  const address = document.getElementById("event-location").innerHTML;
  const mapLink = document.getElementById("map-link");

  mapLink.href = `https://www.google.com/maps?q=${encodeURIComponent(address)}`;
}

function toggleEventActions(data) {
  /*Display the add to calendar and event registration buttons
  if data.content is an empty string. 
  */
  const addToCalendarSection = $("#add-to-calendar");
  const eventRegButton = $("#add-to-calendar");

  if (data.content.trim() == "") {
    addToCalendarSection.show();
    eventRegButton.show();
  } else {
    addToCalendarSection.hide();
    eventRegButton.hide();
  }
}

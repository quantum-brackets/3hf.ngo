// $('#show-event-detail').click(function() {
//     var eventPk = $(this).data('event-pk');
//     var offset = $(this).data('offset');

//     $.get('/load_more_comments/', {post_id, offset}, function(data) {
//         $('#comments-list').append(data.html);
//         $('#load-more-comments').data('offset', offset + 6);
//         if ( !data.has_more_comments) {
//             $('#load-more-comments').hide();
//         }
//     }).fail(function() {
//         console.log('Failed to load more comments');
//     });;
// });

$(document).ready(function () {
  // Function to fetch and display event details
  function fetchEventDetails(eventPk) {
    $.ajax({
      url: "/events/upcoming/" + eventPk + "/",
      type: "GET",
      success: function (data) {
        $("#event-theme").text(data.theme);
        $("#event-description").text(data.description);
        $("#event-time").text(data.time);
        $("#event-date").text(formatDate(data.date));
        $("#event-location").text(data.location);
        $("#event-image").attr("src", data.image_url);

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
  console.log({ urlParams });
  if (urlParams.has("event")) {
    var eventPk = urlParams.get("event");
    fetchEventDetails(eventPk);
  } 

  // Event listener for click events to show event details
  $(".show-event-detail").click(function () {
    var eventPk = $(this).data("event-pk");
    fetchEventDetails(eventPk);

    // Update the URL with the event pk
    var newUrl =
      window.location.protocol +
      "//" +
      window.location.host +
      window.location.pathname +
      "?event=" +
      eventPk;
    window.history.pushState({ path: newUrl }, "", newUrl);
  });

  // Handle browser back/forward buttons
  window.onpopstate = function (event) {
    if (event.state && event.state.path) {
      console.log({ state: event.state });
      var eventPk = new URL(event.state.path).searchParams.get("event");
      fetchEventDetails(eventPk);
    }
  };
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

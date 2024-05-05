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

$(document).ready(function() {
    $('.show-event-detail').click(function() {
        console.log("Clicked event")
      var eventPk = $(this).data('event-pk');
      $.ajax({
        url: eventPk + '/',
        type: 'GET',
        success: function(data) {
            $('#event-theme').text(data.theme);
            $('#event-description').text(data.description);
            $('#event-time').text(data.time);
            // $('#event-date').text(data.date);
            $('#event-date').text(formatDate(data.date))
            $('#event-location').text(data.location);
            $('#event-image').attr('src', data.image_url);

            $("#event-details").removeClass("hidden");

            scrollToEventDetail()
        },
        error: function(xhr, status, error) {
          console.error('Error', xhr.responseText);
        }
      });
    });
  });

  function scrollToEventDetail() {
    var eventDetailsOffset = $('#event-details').offset().top;
    $('html, body').animate({
        scrollTop: eventDetailsOffset
    }, 'slow');
  }

  function formatDate(dateString) {
    const date = new Date(dateString);
    const options = { month: 'long', day: 'numeric', year: 'numeric' };
    return date.toLocaleDateString('en-US', options);
}
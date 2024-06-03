$(document).ready(function () {
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        // Check if the cookie name matches the CSRF token cookie name
        if (cookie.substring(0, name.length + 1) === name + "=") {
          // Extract the CSRF token value
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  var csrftoken = getCookie("csrftoken");

  $("#event-register-form").on("submit", function (event) {
    event.preventDefault();

    const event_id = $("#event-id-input").val()

   
    const formData = {
        event_id,
        registrant_name: $("#registrant-name").val(),
        registrant_email: $("#registrant-email").val(),
        registrant_phone_number: $("#registrant-phone-number").val(),
        additional_message: $("#additional-message").val(),
      };

    var form = $(this);
    
    console.log({form});
    // var formData = form.serialize(); // Serialize form data
    console.log({ formData });

    $.ajax({
      type: "POST",
      url: `${event_id}/register/`,
      data: JSON.stringify(formData),
      headers: { "Content-Type": "application/json", "X-CSRFToken": csrftoken },
      success: function (response) {
        if (response.success) {
          alert(response.message); // Display success message
          form[0].reset(); // Reset the form
        } else {
          // Display error messages
        //   var errorMessages = "";
        //   $.each(response.errors, function (key, value) {
        //     errorMessages += value + "\n";
        //   });
        alert(response.message);
        }
      },
      error: function (xhr, errmsg, err) {
        alert("There was an error with your request: " + errmsg);
      },
    });
  });
});

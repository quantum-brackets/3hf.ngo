$(document).ready(function () {
  var csrftoken = getCookie("csrftoken");

  $("#event-register-form").on("submit", function (event) {
    event.preventDefault();

    // Get the event id from the form
    const event_id = $("#event-id-input").val();

    const formData = {
      event_id,
      registrant_name: $("#registrant-name").val(),
      registrant_email: $("#registrant-email").val(),
      registrant_phone_number: $("#registrant-phone-number").val(),
      additional_message: $("#additional-message").val(),
    };

    var form = $(this);
    const submitButton = $("#event-registration-button");
    setSubmitButtonState(submitButton, false);

    const url = `${window.location.origin}/events/${event_id}/register/`;
    $.ajax({
      type: "POST",
      url,
      data: JSON.stringify(formData),
      headers: { "Content-Type": "application/json", "X-CSRFToken": csrftoken },
      success: function (response) {
        if (response.success) {
          showResponseModal("Registration successful!", response);
          setSubmitButtonState(submitButton, true);
          form[0].reset();
        } else {
          showResponseModal("Oops!", response);
          setSubmitButtonState(submitButton, true);
        }
      },
      error: function (xhr, errmsg, err) {
        showResponseModal("Server error ");
        setSubmitButtonState(submitButton, true);
      },
    });
  });
});

function showResponseModal(headerResponse, data = undefined) {
  const modalMessage = document.getElementById("modal-message");
  const responseHeader = document.getElementById("modal-header");

  responseHeader.textContent = headerResponse;
  if (data) {
    modalMessage.textContent = data.message;
  }
  const modalToggle = document.querySelector(
    '[data-modal-toggle="response-modal"]'
  );
  modalToggle.click();
}

/**
 * Get the CSRF token value from the cookie
 * @param {string} name - The name of the CSRF token cookie
 * @returns {string} The CSRF token value
 */
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


/**
 * Set the state of the submit button
 * @param {object} submitButton - The submit button element
 * @param {boolean} isDisabled - true to enable the button, false to disable
 */
function setSubmitButtonState(submitButton, isEnabled) {
  if (isEnabled) {
    submitButton.removeClass("disabled");
    submitButton.text("Register");
  } else {
    submitButton.addClass("disabled");
    submitButton.text("Registering...");
  }
}

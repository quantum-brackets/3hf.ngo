const contactUsForm = document.getElementById("contact-form");
//  const submitButton = document.getElementById("contact-form-button");
const submitButton = document.querySelector('button[type="submit"]');

const fullName = document.getElementById("id_name");
const email = document.getElementById("id_email");
const phoneNumber = document.getElementById("id_phone_number");
const message = document.getElementById("id_message");

function validateForErrors() {
  const errors = [];
  if (!fullName.value.trim() | (fullName.value.trim() === "")) {
    errors.push(fullName.id);
  }

  if (!email.value.trim() || email.value.trim() === "") {
    errors.push(email.id);
  }

  if (!message.value.trim() || message.value.trim() === " ") {
    errors.push(message.id);
  }
  return errors;
}

async function handleFormSubmission(event) {
  event.preventDefault();
  const errors = validateForErrors();

  if (errors.length > 0) {
    const formError = document.getElementById("contact-form-error");
    formError.classList.remove("hidden");

    errors.map((errorId) => {
      const errorElement = document.getElementById(errorId);
      errorElement.style.border = "3px solid red";
    });

    return false;
  } else {
    submitButton.innerHTML = "Sending...";

    // custom .disabled class declared in input.css
    submitButton.classList.add("disabled");

    try {
      const response = await sendContactMessageRequest()
      const data = await response.json();
      console.log({ data });

      if (data.success === true) {
        showSuccessModal(data);
        contactUsForm.reset();
      } else {
        console.log("Failure: " + JSON.stringify(data));
      }
    } catch (error) {
      console.log({ errorOnSubmission: error });
    } finally {
      submitButton.innerHTML = "Send Message";
      submitButton.classList.remove("disabled");
    }
  }
}

contactUsForm.addEventListener("submit", handleFormSubmission);

const sendContactMessageRequest = async () => {
  const url = "/contact";
  const formData = {
    name: fullName.value,
    email: email.value,
    phoneNumber: phoneNumber.value,
    message: message.value,
  };

  return await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken")[0]
        .value,
    },
    body: JSON.stringify(formData),
  });
}

const showSuccessModal = (data) => {
  const responseHeader = document.getElementById("modal-header");
  const modalMessage = document.getElementById("modal-message");

  responseHeader.textContent = 'Your message has been sent!'
  modalMessage.textContent = data.message;
  const modalToggle = document.querySelector(
    '[data-modal-toggle="response-modal"]'
  );
  modalToggle.click();
};

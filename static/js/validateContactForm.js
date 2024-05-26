const contactUsForm = document.getElementById("contact-us-form");

const fullName = document.getElementById("id_name");
const email = document.getElementById("id_email");
const phoneNumber = document.getElementById("id_phone");
const message = document.getElementById("id_message");

function validateForErrors(error) {
  if (!fullName.value.trim() | (fullName.value.trim() === "")) {
    error.push(fullName.id);
  }

  if (!email.value.trim() || email.value.trim() === "") {
    error.push(email.id);
  }

  if (!message.value.trim() || message.value.trim() === " ") {
    error.push(message.id);
  }
}

function validateContactForm() {
  const errors = [];

  validateForErrors(errors);

  if (errors.length > 0) {
    const formError = document.getElementById("contact-form-error");
    formError.classList.remove("hidden");

    errors.map((errorId) => {
      const errorElement = document.getElementById(errorId);
      errorElement.style.border = "3px solid red";
    });

    return false;
  }

  return true;
}

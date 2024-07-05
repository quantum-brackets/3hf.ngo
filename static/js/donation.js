"use strict";

const paystackForm = document.getElementById("paystack-form");
const stripeForm = document.getElementById("stripe-form");

const showPaystackFormButton = document.getElementById("show-paystack-form");

const showStripeFormButton = document.getElementById("show-stripe-form");

function showPaystackForm() {
  console.log("testing");
  paystackForm.classList.remove("hidden");
  stripeForm.classList.add("hidden");

  showPaystackFormButton.classList.add("border-[#2b599c]");
  showPaystackFormButton.classList.remove("border-[#DFDFDF]");

  showStripeFormButton.classList.add("border-[#DFDFDF]");
  showStripeFormButton.classList.remove("border-[#2b599c]");
}

function showStripeForm() {
  paystackForm.classList.add("hidden");
  stripeForm.classList.remove("hidden");

  showPaystackFormButton.classList.remove("border-[#2b599c]");
  showPaystackFormButton.classList.add("border-[#DFDFDF]");

  showStripeFormButton.classList.add("border-[#2b599c]");
  showStripeFormButton.classList.remove("border-[#DFDFDF]");
}

var paymentForm = document.getElementById("paystack-form");
paymentForm.addEventListener("submit", payWithPaystack, false);

function payWithPaystack() {
  const validate = validatePaystackForm();
  if (validate === false) {
    return;
  }

  var handler = PaystackPop.setup({
    key: "pk_live_fd688998dfd590409c17a3e5787ab670ef0c799a",
    email: document.getElementById("email").value,
    amount: document.getElementById("amount").value * 100, // the amount value is multiplied by 100 to convert to the lowest currency unit
    currency: document.getElementById("currency").value,
    // csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
    callback: handlePaymentCallback,
    onClose: function () {
      alert("Transaction was not completed, window closed.");
    },
  });
  handler.openIframe();
}

function handlePaymentCallback(response) {
  var reference = response.reference;
  console.log({ reference: response.reference });

  if (response.status === "success") {
    paystackForm.reset();
    verifyPayment(reference);
  } else {
    alert("Payment failed. Please try again.");
  }
}

function verifyPayment(reference) {
  console.log({reference})
  fetch("/verify-paystack-payment/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken")[0].value,
    },
    body: JSON.stringify({ reference }),
  }).then((response) => {
    if (response.ok) {
      console.log({ "Server response": response });
      // alert("Donation successful! Thank you.");
      // window.location.href = '/donation-successful/'
    } else {
      console.error("Error submitting donation data:", response.statusText);
      alert("An error occurred. Please try again later.");
    }
  });
}


function validatePaystackForm(e) {
  console.log("Performing validation");
  const amount = document.getElementById("amount").value;
  const email = document.getElementById("email").value;
  const errorText = document.getElementById("paystack-form-error");
 console.log({amount});
  if (!amount || !email) {
    errorText.innerHTML = "Please fill in all required fields.";
    return false;
  }

  const regex = /^[0-9]+$/;

  if (!regex.test(amount)) {
    errorText.innerHTML = "Please enter only numbers in the amount field.";
    return false;
  }

  if (amount <= 0) {
    error.textContent = "Amount must be greater than 0";
    return false;
  }
  return true;
}

function validateStripeForm(e) {
  console.log("Performing validation");
  const amount = document.getElementById("stripe-amount").value;
  console.log({amount});
  const errorText = document.getElementById("stripe-form-error");

  if (!amount) {
    errorText.innerHTML = "Please fill in amount field.";
    e.preventDefault();
    return false;
  }

  const regex = /^[0-9]+$/;

  if (!regex.test(amount)) {
    errorText.innerHTML = "Please enter only numbers in the amount field.";
    // Clear the input field or prevent further input
    e.preventDefault();
    return false;
  }

  if (amount <= 0) {
    error.textContent = "Amount must be greater than 0";
    return false;
  }
  return true;
}

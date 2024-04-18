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
  const validate =  validatePaystack();
  if (validate === false){
    return;
  }

  var handler = PaystackPop.setup({
    key: "pk_test_a6f071d81735bf046577b42fa9ffaaaced47f1db",
    email: document.getElementById("email").value,
    amount: document.getElementById("amount").value * 100, // the amount value is multiplied by 100 to convert to the lowest currency unit
    currency: document.getElementById("currency").value,
    // csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
    ref: generateReference, 
    callback: handlePaymentCallback,
    onClose: function () {
      alert("Transaction was not completed, window closed.");
    },
  });
  handler.openIframe();
}

function handlePaymentCallback(response) {
  var reference = response.reference;
  alert("Payment complete! Reference: " + reference);
  console.log({ reference: response.reference });

  if (response.status === "success") {
    paystackForm.reset();
    verifyPayment(reference);
  } else {
    alert("Payment failed. Please try again.");
  }
}

function verifyPayment(reference) {
  fetch("/verify-paystack-payment/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": document.getElementsByName('csrfmiddlewaretoken')[0].value,
    },
    body: JSON.stringify({ reference }),
  }).then((response) => {
    if (response.ok) {
      console.log({"Server response": response});
      alert("Donation successful! Thank you.");
    } else {
      console.error("Error submitting donation data:", response.statusText);
      alert("An error occurred. Please try again later.");
    }
  });
}

async function generateReference () {
  const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  let reference = '';

  // Generate reference with a combination of numbers and letters
  for (let i = 0; i < length; i++) {
      const randomIndex = Math.floor(Math.random() * characters.length);
      reference += characters.charAt(randomIndex);
  }

  // Add current timestamp to the reference
  const timestamp = new Date().getTime().toString();
  reference += timestamp;
  console.log({reference})

  return reference;
}

function validatePaystack() {
  console.log('Performing validation')
  const amount = document.getElementById('amount').value;
  const email = document.getElementById('email').value;

  if (!amount || !email) {
      const error = document.getElementById("paystack-form-error");
      error.innerHTML = 'Please fill in all required fields.';
      return false;
  }
  return true
}
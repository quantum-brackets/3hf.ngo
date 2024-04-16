const paystackForm = document.getElementById("paystack-form");
const stripeForm = document.getElementById("stripe-form");

const showPaystackFormButton = document.getElementById("show-paystack-form");

const showStripeFormButton = document.getElementById("show-stripe-form");

console.log(showPaystackFormButton);
console.log(showPaystackFormButton);

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
  var handler = PaystackPop.setup({
    key: "pk_test_a6f071d81735bf046577b42fa9ffaaaced47f1db", // Replace with your public key
    email: document.getElementById("email").value,
    amount: document.getElementById("amount").value * 100, // the amount value is multiplied by 100 to convert to the lowest currency unit
    currency: document.getElementById("currency"), // the amount value is multiplied by 100 to convert to the lowest currency unit
    ref: "12jfw34416", // Replace with a reference you generated
    callback: function (response) {
      //this happens after the payment is completed successfully
      var reference = response.reference;
      alert("Payment complete! Reference: " + reference);
      console.log({response});

      if (response.status === "success") {
        // Payment successful, submit donation data (server-side processing)
        fetch("/http://127.0.0.1:8000/", {
          method: "POST",
          body: JSON.stringify({ reference: response.reference }),
        }).then((response) => {
          if (response.ok) {
            // Display success message or redirect to a confirmation page
            alert("Donation successful! Thank you.");
          } 
          // else {
          //   console.error(
          //     "Error submitting donation data:",
          //     response.statusText
          //   );
          //   alert("An error occurred. Please try again later.");
          // }
        });
      } else {
        alert("Payment failed. Please try again.");
      }
      // Make an AJAX call to your server with the reference to verify the transaction
    },
    onClose: function () {
      alert("Transaction was not completed, window closed.");
    },
  });
  handler.openIframe();
}

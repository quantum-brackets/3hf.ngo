const paystackForm = document.getElementById('paystack-form');
const stripeForm = document.getElementById('stripe-form');


function showPaystackForm() {
    paystackForm.classList.remove("hidden");
    stripeForm.classList.add("hidden");
  }

  function showStripeForm() {
    paystackForm.classList.add("hidden");
    stripeForm.classList.remove("hidden");
  }
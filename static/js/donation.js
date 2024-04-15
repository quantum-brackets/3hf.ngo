const paystackForm = document.getElementById("paystack-form");
const stripeForm = document.getElementById("stripe-form");

const showPaystackFormButton = document.getElementById("show-paystack-form");

const showStripeFormButton = document.getElementById("show-stripe-form");

console.log(showPaystackFormButton);
console.log(showPaystackFormButton);

function showPaystackForm() {
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

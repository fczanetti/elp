// This is your test publishable API key.
const stripe = Stripe("pk_test_51OhAamKjQ2xBbvo2Fv2GdibYWYwCRspEgmATtAWfdGMNtxC2QUdKEl7vKCR5jfegsJS6rew1X2rmGAPH20ughioA00RjcjSYcO");

initialize();

// Create a Checkout Session as soon as the page loads
async function initialize() {
  const response = await fetch("/payments/product_page", {
    method: "POST",
  });

  const { clientSecret } = await response.json();

  const checkout = await stripe.initEmbeddedCheckout({
    clientSecret,
  });

  // Mount Checkout
  checkout.mount('#checkout');
}
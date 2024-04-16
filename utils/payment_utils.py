import stripe
from django.conf import settings

def create_stripe_checkout_session(amount, domain):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': amount * 100,
                        'product_data': {
                            'name': 'Donation',
                        }
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/donation-successful?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=domain + '/donate',
        )
        return checkout_session.url
    except Exception as e:
        raise ValueError(str(e))

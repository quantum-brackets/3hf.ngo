from django.http import JsonResponse
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.http import HttpResponseBadRequest
from django.conf import settings
from django.shortcuts import render, redirect
import json
import requests

import stripe

from utils import payment_utils, contact_utils


class HomeView(TemplateView):
    template_name = 'heartsandhands/home.html'

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body.decode('utf-8'))

        try:
            contact_utils.send_message(self, body)
            print("success")
            return JsonResponse(contact_utils.successResponse)
        except Exception as e:
            print('error:', e)
            return JsonResponse({"success": False, 'error': str(e)})


class ContactUsView(TemplateView):
    template_name = "heartsandhands/contact_us.html"

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body.decode('utf-8'))

        try:
            contact_utils.send_message(self, body)
            print("success")
            return JsonResponse(contact_utils.successResponse(body))
        except Exception as e:
            print('error:', e)
            return JsonResponse({"success": False, 'error': str(e)})


class AboutUsView(TemplateView):
    template_name = "heartsandhands/about_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bg_color'] = '#FFFFFF'
        return context


class DonateView(TemplateView):
    template_name = "heartsandhands/donate.html"

    def post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        DOMAIN = settings.DOMAIN
        if request.POST.get("amount") == "" or request.POST.get("amount") == None:
            return HttpResponseBadRequest("amount cannot be empty")

        amount = int(request.POST.get('amount'))
        payment_gateway = request.POST.get('payment_gateway')

        if payment_gateway == 'stripe':
            print("Payment Gateway is stripe")
            try:
                checkout_url = payment_utils.create_stripe_checkout_session(
                    amount, DOMAIN)
                return redirect(checkout_url)
            except Exception as e:
                return HttpResponseBadRequest(str(e))

        elif payment_gateway == 'paystack':
            print("Payment Gateway is paystack")
            # paystack donation is handled entirely on the clientside
        else:
            # Handle invalid gateway choice
            return render(request, 'heartsandhands/donate.html', {'error': 'Invalid payment gateway'})


class DonationSuccessFul(TemplateView):
    template_name = "heartsandhands/donation_success.html"

    def get_context_data(self, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        context = super().get_context_data(**kwargs)
        session_id = self.request.GET.get('session_id')
        if session_id:

            session = stripe.checkout.Session.retrieve(session_id)
            # customer = stripe.Customer.retrieve(session)
            customer = session.customer_details

            context['session'] = session
            context['customer'] = customer

            return context
        return context


def verify_paystack_success(request):
    if request.method == 'POST':
        print("POST data:", request.POST)
        try:
            data = json.loads(request.body.decode('utf-8'))
            reference = data.get('reference')
            print('Reference: ', reference)
            verification_url = f"https://api.paystack.co/transaction/verify/{reference}"
            response = requests.get(verification_url, headers={
                "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"
            })

            if response.status_code == 200:
                data = response.json()
                # print('Verify Paystack Donation Response: ', response.json())
                print('Verify Paystack Donation Response DATA: ', data['data']['reference'])

                if data["data"]['status'] == 'success':
                    print("succesfulpayment")
                else:
                    # Handle unsuccessful verification from Paystack
                    print("Unsuccessful")
            else:
                # Error during verification request
                print(f"Error verifying transaction: {response.text}")
                # ... (handle verification request error)

            return JsonResponse({'message': 'Donation successful!'})
        except Exception as e:
            print(f'Error processing donation: {e}')
            return JsonResponse({'error': 'An error occurred.'}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)


def ads_txt(_):
    return HttpResponse(
        "google.com, pub-3505239651298035, DIRECT, f08c47fec0942fa0",
        content_type="text/plain",
    )

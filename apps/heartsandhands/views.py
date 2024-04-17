from django.http import JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponseBadRequest
from django.conf import settings
from django.shortcuts import render, redirect
import json
import requests

import stripe

from .forms import ContactUsForm
# from utils.email_utils import send_contact_message
from utils import email_utils, payment_utils


class HomeView(TemplateView):
    template_name = 'heartsandhands/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Set the background color for the home view
        context['bg_color'] = '#FCF7CC'
        context["form"] = ContactUsForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']

            email_utils.send_contact_message(
                name, email, phone_number, message)

            return redirect('home')
        else:
            # If the form is not valid, re-render the page with the form and errors
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)


class ContactUsView(TemplateView):
    template_name = "heartsandhands/contact_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bg_color'] = '#06589C'
        context["form"] = ContactUsForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']

            email_utils.send_contact_message(
                name, email, phone_number, message)

            return redirect('contact_us')
        else:
            # If the form is not valid, re-render the page with the form and errors
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)


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

            # Handle Paystack payment logic
            # ... (your Paystack implementation)
            # return render(request, 'donation_success.html')  # Or handle errors
        else:
            # Handle invalid gateway choice
            return render(request, 'heartsandhands/donate.html', {'error': 'Invalid payment gateway'})


class DonationSuccessFul(TemplateView):
    template_name = "heartsandhands/donation_success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session_id = self.request.GET.get('session_id')
        session = stripe.checkout.Session.retrieve(session_id)
        # customer = stripe.Customer.retrieve(session)
        customer = session.customer_details

        context['session'] = session
        context['customer'] = customer

        return context



def verify_paystack_success(request):
    if request.method == 'POST':
        print("POST data:", request.POST)
        try:
            data = json.loads(request.body.decode('utf-8'))
            reference = data.get('reference')
            verification_url = f"https://api.paystack.co/transaction/verify/{reference}"
            response = requests.get(verification_url, headers={
                "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"
            })

            if response.status_code == 200:
                data = response.json()
                if data["data"]['status'] == 'success':
                    # Donation is successful, proceed with your logic
                    print("succesfulpayment")
                    # return "settled"
                else:
                    # Handle unsuccessful verification from Paystack
                    # ... (handle unsuccessful verification)
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
from django.views.generic import TemplateView
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

import stripe

from .forms import ContactUsForm

from django.shortcuts import render, redirect
# from utils.email.utils import send_contact_message
from utils.email_utils import send_contact_message

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

            send_contact_message(name, email, phone_number, message)
            
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

            send_contact_message(name, email, phone_number, message)
            
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
        YOUR_DOMAIN = settings.DOMAIN
        if request.POST.get("amount") == "" or request.POST.get("amount") == None:
            return HttpResponseBadRequest("amount cannot be empty")

        amount = int(request.POST.get('amount'))
        print({amount})


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
                success_url=YOUR_DOMAIN + '/success',  # Make sure to include the trailing slash
                cancel_url=YOUR_DOMAIN + '/cancel',  # Reverse to get the URL name
            )
            return redirect(checkout_session.url)
        except Exception as e:
            return HttpResponseBadRequest(str(e))
from django.views.generic import TemplateView
from .forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect

class HomeView(TemplateView):
    template_name = 'heartsandhands/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Set the background color for the home view
        context['bg_color'] = '#FCF7CC'
        return context


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

            send_mail(
                subject='Contact message from 3hf',
                message=f"Name: {name}\nEmail: {email}\nPhone Number: {phone_number}\n\nMessage: {message}",
                from_email=email,
                recipient_list=['program@3hf.ngo'],
            )
            
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

    

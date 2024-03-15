from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'heartsandhands/home.html'

class ContactUsView(TemplateView):
    template_name = "heartsandhands/contact_us.html"
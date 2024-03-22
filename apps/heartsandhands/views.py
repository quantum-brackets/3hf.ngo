from django.views.generic import TemplateView


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
        return context


class AboutUsView(TemplateView):
    template_name = "heartsandhands/about_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bg_color'] = '#FFFFFF'
        return context

class DonateView(TemplateView):
    template_name = "heartsandhands/donate.html"

    

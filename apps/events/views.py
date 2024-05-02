from django.shortcuts import render
from django.views.generic import TemplateView

from .models import UpcomingEvents


class UpcomingEventsView(TemplateView):
    template_name = "events/upcoming_events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upcoming_events'] = UpcomingEvents.objects.all()
        return context

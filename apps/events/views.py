from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView
from django.template.loader import render_to_string
from .models import UpcomingEvents


class UpcomingEventsView(ListView):
    model = UpcomingEvents
    template_name = "events/upcoming_events.html"
    context_object_name = "upcoming_events"


def event_detail_json(request, pk):
    print('Event pk', pk)
    # event = UpcomingEvents.objects.get(pk=pk)
    event = UpcomingEvents.objects.only(
        "theme", "description", "time", "date", "location", "image",).get(pk=pk)

    print(event)

    data = {
        'theme': event.theme,
        'description': event.description,
        "location": event.location,
        "time": event.time,
        "date": event.date,
        "image_url": event.image.url
    }

    return JsonResponse(data)

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import UpcomingEvents, ConcludedEvents, EventRegistration
from django.shortcuts import get_object_or_404

from . forms import EventRegistrationForm


class UpcomingEventsView(ListView):
    model = UpcomingEvents
    template_name = "events/upcoming_events.html"
    context_object_name = "upcoming_events"


def event_detail_json(request, slug):
    # print('Event pk', pk)
    print('Slug', slug)

    # event = UpcomingEvents.objects.get(pk=pk)
    # event = UpcomingEvents.objects.only(
        # "theme", "description", "time", "date", "location", "image", "slug").get(pk=pk)
    event = get_object_or_404(UpcomingEvents, slug=slug)
    print(event.id)

    data = {
        'id': event.id,
        'theme': event.theme,
        'description': event.description,
        "location": event.location,
        "time": event.time,
        "date": event.date,
        "image_url": event.image.url,
        "slug": event.slug
    }

    return JsonResponse(data)

class ConcludedEventsListView(ListView):
    model = ConcludedEvents
    template_name = 'events/concluded_events_list.html'
    context_object_name = 'concluded_events'

class ConcludedEventsDetailsView(DetailView):
    model = ConcludedEvents
    template_name = 'events/concluded_event_details.html'
    context_object_name = 'concluded_event'


def register_for_event(request, event_id):
    event = get_object_or_404(UpcomingEvents, id=event_id)
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)   # Create the instance but don't save it yet
            registration.event = event  # Set the foreign key field
            registration.save()
            return JsonResponse({'success': True, 'message': 'Thank you for registering!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = EventRegistrationForm()
    return render(request, 'register_for_event.html', {'event': event, 'form': form})
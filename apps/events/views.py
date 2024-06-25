from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from .models import UpcomingEvents, ConcludedEvents, EventRegistration
from django.shortcuts import get_object_or_404
import json
from datetime import datetime, date
from django.db.models import Q


class EventsView(ListView):
    model = UpcomingEvents
    template_name = "events/events.html"
    context_object_name = "upcoming_events"

    def get_queryset(self):
        today = date.today()
        current_time = datetime.now()
        formatted_time = current_time.strftime("%H:%M:%S")

        # return self.model.objects.filter(
        #     Q(date__gt=today) | (Q(date=today) & Q(time__gt=formatted_time))
        # ).order_by('date', 'time').se
        events =  self.model.objects.select_related('concludedevents')
        for event in events:
            print(f"Upcoming Event: {event.theme}")
            print(f"Date: {event.date}")
            
            # Check if the upcoming event has a related concluded event
            if hasattr(event, 'concludedevents'):
                concluded_event = event.concludedevents
                print(f"Concluded cotent: {concluded_event.content}")
            else:
                print("This event has not concluded yet.")
        return events


def event_detail_json(request, slug):
    print('Slug', slug)

    event = get_object_or_404(UpcomingEvents, slug=slug)

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

     # Check if the upcoming event has a related concluded event
    if hasattr(event, 'concludedevents'):
        concluded_event = event.concludedevents
        data['content'] = concluded_event.content
    else:
        data['content'] = ''

    return JsonResponse(data)


def register_for_event(request, event_id):
    body = json.loads(request.body.decode('utf-8'))
    event = UpcomingEvents.objects.get(id=event_id)
    if not event:
        return JsonResponse({'success': False, 'message': 'Event not found'}, status=404)

    if request.method == 'POST':
        try:
            registrant = EventRegistration.objects.create_registrant(**body)
            return JsonResponse({
                'success': True,
                'message': 'Thank you for registering.'
            })
        except Exception as e:
            print('Error:', e)
            error_message = e.messages[0]  # Extract the error message
            return JsonResponse({'success': False, 'message': error_message})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

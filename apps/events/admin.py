from django.contrib import admin


from .models import UpcomingEvents, ConcludedEvents, EventRegistration
from .forms import CreateUpcomingEventForm, ConcludedEventsForm

class ConcludedEventsInline(admin.StackedInline):
    model = ConcludedEvents
    extra= 0
    form = ConcludedEventsForm

class EventRegistrationInline(admin.StackedInline):
    model = EventRegistration
    extra= 0
@admin.register(UpcomingEvents)
class UpcomingEventsAdmin(admin.ModelAdmin):
    model = UpcomingEvents
    form = CreateUpcomingEventForm
    list_display = ['theme', 'date', 'location']
    inlines = [EventRegistrationInline, ConcludedEventsInline]
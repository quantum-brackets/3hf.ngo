from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import UpcomingEvents, ConcludedEvents, SummernoteAttachment
from .forms import CreateUpcomingEventForm, ConcludedEventsForm

class ConcludedEventsInline(admin.StackedInline):
    model = ConcludedEvents
    extra= 0
    form = ConcludedEventsForm

@admin.register(UpcomingEvents)
class UpcomingEventsAdmin(admin.ModelAdmin):
    model = UpcomingEvents
    form = CreateUpcomingEventForm
    list_display = ['theme', 'date', 'location']
    inlines = [ConcludedEventsInline]

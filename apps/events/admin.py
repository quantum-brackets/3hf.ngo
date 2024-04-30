from django.contrib import admin

from .models import UpcomingEvents
from .forms import CreateUpcomingEventForm

@admin.register(UpcomingEvents)
class UpcomingEventsAdmin(admin.ModelAdmin):
    model = UpcomingEvents
    add_form = CreateUpcomingEventForm
    list_display = ['theme', 'date', 'location']
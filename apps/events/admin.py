from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import UpcomingEvents, PastEvents, SummernoteAttachment
from .forms import CreateUpcomingEventForm

@admin.register(UpcomingEvents)
class UpcomingEventsAdmin(admin.ModelAdmin):
    model = UpcomingEvents
    form = CreateUpcomingEventForm
    list_display = ['theme', 'date', 'location']

@admin.register(PastEvents)
class PastEventsAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    list_display = ['event',  'created_at',]

admin.site.register(SummernoteAttachment)
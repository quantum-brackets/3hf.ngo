from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils import timezone


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

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        """
        Customize the form field for the 'date' field to include a custom validation error
        message and a validation function.

        Args:
            db_field (django.db.models.Field): The database field being processed.
            request (django.http.HttpRequest): The current HTTP request object.
            kwargs (dict): Additional keyword arguments for the form field.

        Returns:
            django.forms.Field: The customized form field for the 'date' field.
        """
        
        formfield = super().formfield_for_dbfield(db_field, request, **kwargs)
        if db_field.name == 'date':
            formfield.error_messages = {'invalid': 'Date must be greater than the current date'}
            if not request.path.endswith('/change/'):  # Check if it's not an update request
                formfield.validators.append(self.validate_date)
        return formfield

    def validate_date(self, value):
        if value <= timezone.now().date():
            raise ValidationError('Date must be greater than the current date')
from django_summernote.widgets import SummernoteWidget
from django.forms import ModelForm
from django import forms

from .models import UpcomingEvents, ConcludedEvents, EventRegistration


class CreateUpcomingEventForm(ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'maxlength': 250}),
    )

    class Meta:
        model = UpcomingEvents
        fields = ['theme', 'description', 'date', "time", "location", "image"]


class ConcludedEventsForm(forms.ModelForm):
    class Meta:
        model = ConcludedEvents
        fields = ('content',)
        widgets = {
            'content': SummernoteWidget(),
        }


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['registrant_email', 'registrant_name',
              'registrant_phone_number', 'additional_message']

from django.forms import ModelForm
from django.core.validators import MaxLengthValidator
from django import forms

from .models import UpcomingEvents, ConcludedEvents


class CreateUpcomingEventForm(ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'maxlength': 250}),
        validators=[MaxLengthValidator(250)]
    )
      
    class Meta:
        model = UpcomingEvents
        fields = ['theme', 'description', 'date', "time", "location", "image"]

from django_summernote.widgets import SummernoteWidget

class ConcludedEventsForm(forms.ModelForm):
    class Meta:
        model = ConcludedEvents
        fields = ('content',)
        widgets = {
            'content': SummernoteWidget(),
        }
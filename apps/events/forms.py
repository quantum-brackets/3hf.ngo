from django.forms import ModelForm
from django.core.validators import MaxLengthValidator
from django import forms

from .models import UpcomingEvents, PastEvents


class CreateUpcomingEventForm(ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'maxlength': 250}),
        validators=[MaxLengthValidator(250)]
    )
      
    class Meta:
        model = UpcomingEvents
        fields = ['theme', 'description', 'date', "time", "location", "image"]

from django_summernote.widgets import SummernoteWidget

class PastEventsForm(forms.ModelForm):
    class Meta:
        model = PastEvents
        fields = ('content',)
        widgets = {
            'content': SummernoteWidget(),
        }
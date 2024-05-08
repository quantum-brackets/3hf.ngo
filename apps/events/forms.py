from django.forms import ModelForm
from django.core.validators import MaxLengthValidator
from django import forms

from .models import UpcomingEvents


class CreateUpcomingEventForm(ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'maxlength': 250}),
        validators=[MaxLengthValidator(250)]
    )
      
    class Meta:
        model = UpcomingEvents
        fields = ['theme', 'description', 'date', "time", "location", "image"]

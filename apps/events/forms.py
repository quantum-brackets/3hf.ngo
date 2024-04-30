from django.forms import ModelForm

from .models import UpcomingEvents


class CreateUpcomingEventForm(ModelForm):
    class Meta:
        model = UpcomingEvents
        fields = ['theme', 'description', 'date', "time", "location", "image"]

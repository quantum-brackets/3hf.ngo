from django.db import models
from django.template.defaultfilters import slugify

from cloudinary.models import CloudinaryField
from django_summernote.models import AbstractAttachment

from . managers import EventRegistrationManager

class UpcomingEvents(models.Model):
    theme = models.CharField(max_length=200)
    description = models.TextField()
    time = models.TimeField()
    date = models.DateField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/uploads')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    slug = models.SlugField(
        max_length=70,
        null=True,
        blank=True,
        editable=False
    )

    class Meta:
        verbose_name = "event"
        verbose_name_plural = "events"

    def __str__(self):
        return f"{self.theme.title()}"

    def save(self, *args, **kwargs):
        slug = f'{self.theme}-{self.date}'
        if not self.slug:
            self.slug = slugify(slug)
        return super().save(*args, **kwargs)


class ConcludedEvents(models.Model):
    event = models.OneToOneField(UpcomingEvents, on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    class Meta:
        verbose_name = "Concluded event"
        verbose_name_plural = "Concluded events"

    def __str__(self):
        return f"{self.event.theme.title()}"

    def save(self, *args, **kwargs):
        slug = self.event.slug
        if not self.slug:
            self.slug = slugify(slug)
        return super().save(*args, **kwargs)


class EventRegistration(models.Model):
    event = models.ForeignKey(
        UpcomingEvents, related_name='events', on_delete=models.SET_NULL, null=True)
    registrant_name = models.CharField(blank=False, max_length=250)
    registrant_email = models.EmailField(blank=False, max_length=250)
    registrant_phone_number = models.CharField(blank=False, max_length=25)
    additional_message = models.TextField(
        blank=True, null=True, max_length=250)
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EventRegistrationManager()

    def __str__(self):
        return f"{self.registrant_name} - {self.registrant_email}"


    class Meta:
        verbose_name = "Registered person"
        verbose_name_plural = "registered persons"

        constraints = [
            models.UniqueConstraint(
                fields=['event_id', 'registrant_email',
                        'registrant_phone_number'],
                name='Duplicated registration',
                violation_error_message='Duplicate registration'
            ),
        ]


class SummernoteAttachment(AbstractAttachment):
    file = CloudinaryField('image')

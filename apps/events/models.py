from django.db import models
from django.template.defaultfilters import slugify

class UpcomingEvents(models.Model):
    theme = models.CharField(max_length=200)
    description = models.TextField()
    time = models.TimeField()
    date = models.DateField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/uploads')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=70, null=True, blank=True, editable=False)

    class Meta:
        verbose_name = "Upcoming event"
        verbose_name_plural = "Upcoming events"
        
    def __str__(self):
        return f"{self.theme.title()}"
 
    def save(self, *args, **kwargs): 
        slug = f'{self.theme}-{self.date}'
        if not self.slug:
            self.slug = slugify(slug)
        return super().save(*args, **kwargs)


class PastEvents(models.Model):
    event = models.OneToOneField(UpcomingEvents, on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Past event"
        verbose_name_plural = "Past events"

    def __str__(self):
        return f"{self.event.theme.title()}"
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
        
    def save(self, *args, **kwargs): 
        slug = f'{self.theme}-{self.date}'
        if not self.slug:
            self.slug = slugify(slug)
        return super().save(*args, **kwargs)

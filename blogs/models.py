from django.db import models
# Create your models here.
from django.conf import settings

from django.utils import timezone


class Resource(models.Model):
    
    title = models.CharField(max_length=200)
    
    pdf = models.FileField(upload_to='resource/pdfs/')
    created_date = models.DateTimeField(default=timezone.now)
    
    published_date = models.DateTimeField(blank=True, null=True)

    
  

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

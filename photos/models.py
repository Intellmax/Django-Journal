from django.db import models
from django.utils import timezone



#Photos
class Photo(models.Model):
  title = models.CharField("Photo Name", max_length=100)
  img = models.ImageField("Photo", upload_to='images/')
  counter = models.PositiveIntegerField('counter',default = 0)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)
  
class Meta:
    ordering = ['title']
    verbose_name = 'Photo'
    verbose_name_plural = 'Photos'
def __str__(self):
    return self.title


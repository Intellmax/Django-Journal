from django.db import models


#Photos
class Photo(models.Model):
  title = models.CharField("Photo Name", max_length=100)
  img = models.ImageField("Photo", upload_to='images/')
class Meta:
    ordering = ['title']
    verbose_name = 'Photo'
    verbose_name_plural = 'Photos'
def __str__(self):
    return self.title

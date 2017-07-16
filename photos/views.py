from django.shortcuts import render
from .models import Photo


def my_photo (request):
	photos = Photo.objects.all()
	return render (request, 'photos/my_photo.html', {'photos':photos})
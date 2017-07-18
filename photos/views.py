from django.shortcuts import render, get_object_or_404
from .models import Photo


def my_photo (request):
	photos = Photo.objects.all()
	return render (request, 'photos/my_photo.html', {'photos':photos})

def photo_detail (request, pk):
	photo = get_object_or_404 (Photo, pk=pk)
	return render(request, 'photos/photo_detail.html', {'photo': photo})




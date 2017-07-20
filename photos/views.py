from django.shortcuts import render, get_object_or_404
from .models import Photo
from django.db.models import F
from django.utils import timezone


def my_photo (request):
	photos = Photo.objects.all()
	return render (request, 'photos/my_photo.html', {'photos':photos})

def photo_detail (request, pk):
	photo = get_object_or_404 (Photo, pk=pk)
	count = Photo.objects.get (pk=pk)
	count.counter = F('counter')+1
	count.save()
	return render(request, 'photos/photo_detail.html', {'photo': photo, 'count':count})

def popular(request):
    popphotos = Photo.objects.filter(published_date__lte=timezone.now()).order_by('-counter')[:5]
    return render(request, 'photos/popular.html', {'popphotos': popphotos})




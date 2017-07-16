from django.contrib import admin
from photos.models import Photo

#For Photo
class PhotoAdmin(admin.ModelAdmin):
    fieldsets = [(None, {"fields": ['title', 'img']})]
    list_display = ['title']
    ordering = ['title']

#Registering
admin.site.register(Photo, PhotoAdmin)

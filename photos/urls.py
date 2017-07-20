from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.my_photo, name='my_photo'),
    url(r'^photo_detail/(?P<pk>[0-9]+)/$', views.photo_detail, name='photo_detail'),
    url(r'^popular/$', views.popular, name='popular'),
    
]







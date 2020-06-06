from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='awards-home'),
    path('about', views.about, name='awards-about')
 
]
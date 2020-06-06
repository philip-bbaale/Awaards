from django.urls import path
from . import views

urlpatterns = [
    path('newpost', views.new_post, name='new_post'), 
]
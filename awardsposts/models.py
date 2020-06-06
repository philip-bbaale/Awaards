from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    project_title = models.CharField(max_length=100)
    project_image = models.ImageField(upload_to='post_images')
    project_description = models.TextField(max_length=300)
    project_url = models.CharField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_title
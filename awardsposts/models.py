from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Post(models.Model):
    project_title = models.CharField(max_length=100)
    project_image = models.ImageField(upload_to='post_images')
    project_description = models.TextField(max_length=300)
    project_url = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    design_rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])
    usability_rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])
    content_rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return self.project_title
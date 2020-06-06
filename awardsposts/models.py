from django.db import models

# Create your models here.
class Post(models.Model):
    project_title = models.CharField(max_length=100)
    project_image = models.ImageField(upload_to='post_images')
    project_description = models.TextField(max_length=300)
    project_url = models.CharField()

    def __str__(self):
        return self.project_title
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
    
    def __str__(self):
        return self.project_title

    @classmethod
    def no_of_ratings(self):
        ratings = Ratings.objects.filter(post=self)
        return len(ratings)

    @classmethod
    def avg_rating(self):
        sum = 0
        ratings = Ratings.objects.filter(post=self)
        for rating in ratings:
            sum += rating.stars

        if len(ratings) > 0:
            return sum/len(ratings)
        else:
            return 0

class Ratings(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    design_rating = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    usability_rating = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    content_rating = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author


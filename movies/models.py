from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    image_url = models.URLField(default='https://via.placeholder.com/150')
    description = models.TextField()
    year = models.IntegerField(default=2000)
    likes = models.IntegerField(default=0)
    followed_by = models.ManyToManyField(User, related_name='followed_movies', blank=True, default=None)
    release_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

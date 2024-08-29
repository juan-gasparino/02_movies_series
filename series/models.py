from django.db import models
from django.contrib.auth.models import User

class Serie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    image_url = models.URLField(default='https://via.placeholder.com/150')
    description = models.TextField()
    seasons = models.IntegerField(default=1)
    year = models.IntegerField(default=2000)
    likes = models.IntegerField(default=0)
    followed_by = models.ManyToManyField(User, related_name='followed_series', blank=True, default=None)
    first_episode = models.DateTimeField(auto_now_add=True)
    last_episode = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

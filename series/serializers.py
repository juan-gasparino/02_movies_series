from rest_framework import serializers
from .models import Serie

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ['id', 'title', 'genre', 'image_url', 'description', 'seasons', 'year', 'likes', 'followed_by', 'first_episode', 'last_episode']
        read_only_fields = ['likes', 'followed_by']
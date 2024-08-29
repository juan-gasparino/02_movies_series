from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'image_url', 'description', 'year', 'likes', 'followed_by', 'release_at']
        read_only_fields = ['likes', 'followed_by']
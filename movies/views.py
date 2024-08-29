from rest_framework import generics, permissions, status
from rest_framework.response import Response
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from api_movies_series.views import IsAdminUserOrReadOnly


class MovieListCreate(generics.ListCreateAPIView):
    """
    API list movies and create a new movie.
    """
    queryset = Movie.objects.all().order_by('-pk')
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    error_message = 'You do not have permission to perform this action.'


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API show detail, update and delete a movie.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    error_message = 'You do not have permission to perform this action.'


class MovieLikeView(APIView):
    """
    API view to like a movie.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        movie.likes += 1
        movie.save()
        return Response({
            'status': 'movie liked', 
            'likes': movie.likes
        }, status=status.HTTP_200_OK)


class MovieFollowView(APIView):
    """
    API view to follow a movie.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        user = request.user
        if movie.followed_by.filter(id=user.id).exists():
            movie.followed_by.remove(user)
            message = 'unfollowed'
        else:
            movie.followed_by.add(user)
            message = 'followed'
        movie.save()
        return Response({
            'status': f'movie {message}', 
            'followers': movie.followed_by.count()}, status=status.HTTP_200_OK)
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from series.models import Serie
from series.serializers import SerieSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from api_movies_series.views import IsAdminUserOrReadOnly


class SerieListCreate(generics.ListCreateAPIView):
    """
    API list series and create a new serie.
    """
    queryset = Serie.objects.all().order_by('-pk')
    serializer_class = SerieSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    error_message = 'You do not have permission to perform this action.'


class SerieDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API show detail, update and delete a serie.
    """
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    error_message = 'You do not have permission to perform this action.'


class SerieLikeView(APIView):
    """
    API view to like a movie.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        movie = get_object_or_404(Serie, pk=pk)
        movie.likes += 1
        movie.save()
        return Response({
            'status': 'serie liked', 
            'likes': movie.likes
        }, status=status.HTTP_200_OK)


class SerieFollowView(APIView):
    """
    API view to follow a movie.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        movie = get_object_or_404(Serie, pk=pk)
        user = request.user
        if movie.followed_by.filter(id=user.id).exists():
            movie.followed_by.remove(user)
            message = 'unfollowed'
        else:
            movie.followed_by.add(user)
            message = 'followed'
        movie.save()
        return Response({
            'status': f'serie {message}', 
            'followers': movie.followed_by.count()
        }, status=status.HTTP_200_OK)
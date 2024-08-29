from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from movies.models import Movie
from .serializers import UserSerializer
from movies.serializers import MovieSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404



class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class CreateUserView(generics.CreateAPIView):
    """
    API view to register a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
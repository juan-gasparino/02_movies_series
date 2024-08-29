from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieListCreate.as_view(), name='movie_list'),
    path('movies/<int:pk>/', views.MovieDetail.as_view(), name='movie_detail'),
    path('movies/<int:pk>/like/', views.MovieLikeView.as_view(), name='movie-like'),
    path('movies/<int:pk>/follow/', views.MovieFollowView.as_view(), name='movie-follow'),
]
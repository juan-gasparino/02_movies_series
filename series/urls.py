from django.urls import path
from . import views

urlpatterns = [
    path('series/', views.SerieListCreate.as_view(), name='serie_list'),
    path('series/<int:pk>/', views.SerieDetail.as_view(), name='serie_detail'),
    path('series/<int:pk>/like/', views.SerieLikeView.as_view(), name='serie-like'),
    path('series/<int:pk>/follow/', views.SerieFollowView.as_view(), name='serie-follow'),
]
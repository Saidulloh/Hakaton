from django.urls import path

from apps.favorite.views import *


urlpatterns = [
    path('list/', FavoriteAPIView.as_view()),
    path('detail/<int:pk>/', FavoriteDetailAPIView.as_view()),
    path('delete/<int:pk>/', FavoriteDeleteAPIView.as_view()),
    path('create/', FavoriteCreateAPiView.as_view()),
]  
from django.urls import path

from apps.users.views import *

urlpatterns = [
    # direction
    path('direction/', ListCreateAPIView.as_view()),
    path('direction/<int:pk>/', CRUDirectionAPIView.as_view()),
    # developer
    path('list/', ListDeveloperAPIView.as_view()),
    path('create/', CreateDeveloperAPIView.as_view()),
    path('detail/<int:pk>/', DetailDeveloperAPIView.as_view()),
    path('update/<int:pk>/', UpdateDeveloperAPIView.as_view()),
    path('delete/<int:pk>/', DeleteDeveloperAPIView.as_view()),
    # client
    path('client/', ListCreateClientAPIView.as_view()),
    path('client/<int:pk>/', CRUDClientAPIView.as_view()),
]
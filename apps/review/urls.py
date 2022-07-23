from django.urls import path

from apps.review.views import *

urlpatterns = [
    # review
    path('list/', ListReviewAPIView.as_view()),
    path('create/', CreateReviewAPIView.as_view()),
    path('detail/<int:pk>/', DetailReviewAPIView.as_view()),
    path('update/<int:pk>/', UpdateReviewAPIView.as_view()),
    path('delete/<int:pk>/', DeleteReviewAPIView.as_view()),
] 
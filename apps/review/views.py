from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response

from apps.review.serializers import ReviewSerializer
from apps.review.models import Review
from apps.review.permissions import IsOwner


class ListReviewAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        f = Review.objects.filter(owner=request.user)
        
        r = 0
        d = []
        for i in f:
            r+= int(i.star)
            d.append(i.star)
        if len(d):
            r = round(r / len(d), 1)
        else:
            return Response({'Напоминание': 'Отзывов нет'})
        return Response({r:ReviewSerializer(f, many=True).data})


class DetailReviewAPIView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class DeleteReviewAPIView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwner, IsAdminUser]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class CreateReviewAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class UpdateReviewAPIView(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwner or IsAdminUser]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
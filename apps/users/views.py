from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from apps.review.models import Review
from rest_framework.response import Response

from apps.users.permissions import IsOwnerOrReadOnly
from apps.users.serializers import *
from apps.users.models import *


class ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = [IsAdminUser]


class CRUDirectionAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = [IsAdminUser]


class ListDeveloperAPIView(generics.ListAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperMinSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class DetailDeveloperAPIView(generics.RetrieveAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperShowSerializer
    permission_classes = [IsOwnerOrReadOnly or IsAdminUser]


class DeleteDeveloperAPIView(generics.DestroyAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperFullSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class CreateDeveloperAPIView(generics.CreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperFullSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly]


class UpdateDeveloperAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = DeveloperFullSerializer
    permission_classes = [IsOwnerOrReadOnly or IsAdminUser]


class ListCreateClientAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class CRUDClientAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsOwnerOrReadOnly or IsAdminUser]
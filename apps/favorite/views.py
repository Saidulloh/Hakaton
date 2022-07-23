from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.favorite.permissions import IsOwner
from apps.favorite.serializers import FavoriteSerializer, FavoriteFullSerializer
from apps.favorite.models import Favorite


class FavoriteAPIView(generics.ListAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteFullSerializer
    permission_classes = [IsOwner]

    def get(self, request):
        f = Favorite.objects.filter(user=request.user)
        return Response(FavoriteSerializer(f, many=True).data)


class FavoriteDetailAPIView(generics.RetrieveAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsOwner or IsAdminUser]


class FavoriteDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsOwner or IsAdminUser]


class FavoriteCreateAPiView(generics.CreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
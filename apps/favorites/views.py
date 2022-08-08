from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

from apps.favorites.permissions import IsOwner
from apps.favorites.serializers import FavoriteSerializer, FavoriteFullSerializer
from apps.favorites.models import Favorite


class FavoriteAPIView(generics.ListAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteFullSerializer
    permission_classes = [IsOwner or IsAdminUser]

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

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except:
            return Response({'Error':'You are cannot add yourself to favorite list and more 1 time'})
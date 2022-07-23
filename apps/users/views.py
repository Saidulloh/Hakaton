from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from apps.review.models import Review
from rest_framework.response import Response

from apps.users.permissions import IsOwnerOrReadOnly
from apps.users.serializers import *
from apps.users.models import *
from rest_framework.pagination import PageNumberPagination

from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend
from apps.users.service import DeveloperFilter


class Developerpagination(PageNumberPagination):
    #Количество записей для пагинации 
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

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
    pagination_class = Developerpagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filter
    filterset_class = DeveloperFilter
    # Поиск
    search_fields = [
            'city',
            'direction',
            'lvl',
            'gender',
            ]       
    # сортировка                                       
    # ordering_fields = [
    #             '',   
    #             ]


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
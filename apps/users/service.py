from django_filters import rest_framework as filters
from apps.users.models import Developer

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class DeveloperFilter(filters.FilterSet):
    city = CharFilterInFilter(field_name='city', lookup_expr='in')
    lvl = CharFilterInFilter(field_name='color', lookup_expr='in')
    gender = CharFilterInFilter(field_name='gender', lookup_expr='in')
    # material = CharFilterInFilter(field_name='material', lookup_expr='in')
    # brand = CharFilterInFilter(field_name='brand', lookup_expr='in')
    # owner = CharFilterInFilter(field_name='owner', lookup_expr='in')

    class Meta:
        model = Developer
        fields = ['city', 'lvl', 'gender']




from django_filters import rest_framework as filters
from apps.users.models import User

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class DeveloperFilter(filters.FilterSet):
    city = CharFilterInFilter(field_name='city', lookup_expr='in')
    lvl = CharFilterInFilter(field_name='color', lookup_expr='in')
    gender = CharFilterInFilter(field_name='gender', lookup_expr='in')

    class Meta:
        model = User
        fields = ['city', 'lvl', 'gender']
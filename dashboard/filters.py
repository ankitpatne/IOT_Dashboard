from .models import Station
import django_filters

class StationFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Station
        fields = ['name', 'status']


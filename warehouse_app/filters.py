import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class DeviceFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='gte')
    serial_number = CharFilter(field_name='serial_number', lookup_expr='icontains')

    class Meta:
        model = Device
        fields = '__all__'
        exclude = ['contract', 'expiration_date', 'renewal_date', 'host_name', 'make', 'model', 'place', 'user']

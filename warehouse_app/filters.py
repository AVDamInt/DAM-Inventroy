import django_filters
from django_filters import DateFilter, CharFilter, ChoiceFilter
from .models import *


class DeviceFilter(django_filters.FilterSet):
    contract = CharFilter(field_name='contract', lookup_expr='icontains')
    serial_number = CharFilter(field_name='serial_number', lookup_expr='icontains')
    model = CharFilter(field_name='model', lookup_expr='icontains')
    status = ChoiceFilter(choices=Device.IS_AVAILABLE_CHOICES)
    user = CharFilter(field_name='user__name', lookup_expr='icontains')

    class Meta:
        model = Device
        fields = '__all__'
        exclude = ['contract', 'expiration_date', 'renewal_date', 'host_name', 'make', 'memory', 'memory_unit',
                   'hard_disk', 'hard_disk_unit', 'cpu', 'place', 'user', 'user_history']


class PlaceFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    city = CharFilter(field_name='city', lookup_expr='icontains')
    country = CharFilter(field_name='country', lookup_expr='icontains')

    class Meta:
        model = Place
        fields = '__all__'
        exclude = ['address', 'cap', 'plan']


class DeviceUserFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    surname = CharFilter(field_name='surname', lookup_expr='icontains')
    email = CharFilter(field_name='email', lookup_expr='icontains')

    class Meta:
        model = DeviceUser
        fields = '__all__'
        exclude = ['role']

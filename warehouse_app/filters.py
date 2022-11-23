import django_filters
from django_filters import DateFilter, CharFilter

from .models import DeviceUser


class DeviceUserFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name')

    class Meta:
        model = DeviceUser
        fields = '__all__'

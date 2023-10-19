import django_filters
from django_filters import DateFilter, CharFilter, ChoiceFilter
from .models import *
from django.db.models import Q


class DeviceFilter(django_filters.FilterSet):
    contract = CharFilter(field_name="contract", lookup_expr="icontains")
    serial_number = CharFilter(field_name="serial_number", lookup_expr="icontains")
    model = CharFilter(field_name="model", lookup_expr="icontains")
    status = ChoiceFilter(choices=Device.IS_AVAILABLE_CHOICES)
    user = CharFilter(field_name="user__name", lookup_expr="icontains")
    user_surname = CharFilter(field_name="user__surname", lookup_expr="icontains")
    q = django_filters.CharFilter(method="search_all_fields", label="Search")

    class Meta:
        model = Device
        fields = "__all__"
        exclude = [
            "contract",
            "expiration_date",
            "renewal_date",
            "host_name",
            "make",
            "memory",
            "memory_unit",
            "hard_disk",
            "hard_disk_unit",
            "cpu",
            "place",
            "user",
            "user_history",
        ]

    def search_all_fields(self, queryset, name, value):
        return queryset.filter(
            Q(contract__icontains=value)
            | Q(serial_number__icontains=value)
            | Q(model__icontains=value)
            | Q(status__icontains=value)
            | Q(user__name__icontains=value)
            | Q(host_name__icontains=value)
            | Q(make__icontains=value)
        )


class PlaceFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains")
    city = CharFilter(field_name="city", lookup_expr="icontains")
    country = CharFilter(field_name="country", lookup_expr="icontains")
    q = django_filters.CharFilter(method="search_all_fields", label="Search")

    class Meta:
        model = Place
        fields = "__all__"
        exclude = ["address", "cap", "plan"]

    def search_all_fields(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value)
            | Q(city__icontains=value)
            | Q(country__icontains=value)
            | Q(address__icontains=value)
            | Q(cap__icontains=value)
            | Q(plan__icontains=value)
        )


class DeviceUserFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains")
    surname = CharFilter(field_name="surname", lookup_expr="icontains")
    email = CharFilter(field_name="email", lookup_expr="icontains")
    q = django_filters.CharFilter(method="search_all_fields", label="Search")

    class Meta:
        model = DeviceUser
        fields = "__all__"
        exclude = ["role"]

    def search_all_fields(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value)
            | Q(surname__icontains=value)
            | Q(email__icontains=value)
            | Q(role__icontains=value)
        )

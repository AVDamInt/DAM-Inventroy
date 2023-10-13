from django.urls import path
from . import views
from .views import SearchResultsListView
urlpatterns = [
    path("device/create", views.create_device, name="device_register"),
    path("", views.DeviceList.as_view(), name="device_list"),
    path(
        "device/read/<int:pk>", views.DeviceDetailView.as_view(), name="device_detail"
    ),
    path(
        "device/update/<int:pk>", views.DeviceUpdateView.as_view(), name="update_device"
    ),
    # path('device/update/<int:pk>', views.update_device, name='update_device'),
    path("device/delete/<id>", views.delete_device, name="device_delete"),
    path("place/create", views.create_place, name="place_register"),
    path("places", views.PlaceList.as_view(), name="place_list"),
    path("place/read/<int:pk>", views.PlaceDetailView.as_view(), name="place_detail"),
    path("place/update/<int:pk>", views.PlaceUpdateView.as_view(), name="update_place"),
    path("place/delete/<int:pk>", views.PlaceDeleteView.as_view(), name="place_delete"),
    path("user/create", views.create_user_device, name="user_register"),
    # path('user/register', views.UserCreateView.as_view(), name='user_register'),
    path("users", views.UserList.as_view(), name="user_list"),
    path("user/<int:pk>", views.DeviceUserDetailView.as_view(), name="user_detail"),
    path(
        "user/edit/<int:pk>", views.DeviceUserUpdateView.as_view(), name="update_user"
    ),
    path("<int:pk>/user", views.UserDeleteView.as_view(), name="user_delete"),
    path("file_upload", views.file_upload, name="file_upload"),
    path("export/devices", views.export_devices, name="export_devices"),
    path("export/places", views.export_places, name="export_places"),
    path("department/create", views.create_department, name='department_register'),
    path("department", views.DepartmentList.as_view(), name="department_list"),
    path("department/read/<int:pk>", views.DepartmentDetailView.as_view(), name="department_detail"),
    path("department/update/<int:pk>", views.DepartmentUpdateView.as_view(), name="update_department"),
    path("department/delete/<int:pk>", views.DepartmentDeleteView.as_view(), name="department_delete"),
    path("search", SearchResultsListView.as_view(),name="search_results"),

]

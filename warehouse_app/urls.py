from django.urls import path
from . import views

urlpatterns = [
    path('', views.device_list, name='device_list'),
    path('device/<int:pk>', views.DeviceDetailView.as_view(), name='device_detail'),
    #path('device/register', views.DeviceCreateView.as_view(), name='device_register'),
    path('device/register', views.create_device, name='device_register'),
    path('<int:pk>/delete', views.DeviceDeleteView.as_view(), name='device_delete'),
    path('place/<int:pk>', views.PlaceDetailView.as_view(), name='place_detail'),
    path('place/register', views.PlaceCreateView.as_view(), name='place_register'),
    path('<int:pk>/place', views.PlaceDeleteView.as_view(), name='place_delete'),
    path('places', views.place_list, name='place_list'),
    path('users', views.UserListView.as_view(), name='user_list'),
    path('user/register', views.UserCreateView.as_view(), name='user_register'),
    path('<int:pk>/user', views.UserDeleteView.as_view(), name='user_delete'),
    path('file_upload', views.file_upload, name='file_upload')
    #path('device/<int:pk>', views.device_details, name='device_details'),
]
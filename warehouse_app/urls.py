from django.urls import path
from . import views

urlpatterns = [
    path('', views.DeviceList.as_view(), name='device_list'),
    path('device/detail/<int:pk>', views.DeviceDetailView.as_view(), name='device_detail'),
    # path('device/register', views.DeviceCreateView.as_view(), name='device_register'),
    path('device/register', views.create_device, name='device_register'),
    path('device/edit/<int:pk>', views.DeviceUpdateView.as_view(), name='update_device'),
    #path('device/delete/<int:pk>', views.DeviceDeleteView.as_view(), name='device_delete'),
    path('<id>/delete', views.delete_device, name='device_delete'),
    path('place/<int:pk>', views.PlaceDetailView.as_view(), name='place_detail'),
    #path('place/register', views.PlaceCreateView.as_view(), name='place_register'),
    path('place/register', views.create_place, name='place_register'),
    path('place/edit/<int:pk>', views.PlaceUpdateView.as_view(), name='update_place'),

    path('<int:pk>/place', views.PlaceDeleteView.as_view(), name='place_delete'),
    #path('place/edit/<int:pk>', views.PlaceUpdateView.as_view(), name='update_place'),
    # path('places', views.PlaceListView.as_view(), name='place_list'),
    path('places', views.PlaceList.as_view(), name='place_list'),
    # path('users', views.UserListView.as_view(), name='user_list'),
    path('users', views.UserList.as_view(), name='user_list'),
    path('user/register', views.UserCreateView.as_view(), name='user_register'),
    path('<int:pk>/user', views.UserDeleteView.as_view(), name='user_delete'),
    path('file_upload', views.file_upload, name='file_upload')
    # path('device/<int:pk>', views.device_details, name='device_details'),
]

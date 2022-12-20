from django.urls import path
from . import views

urlpatterns = [
    path('device/create', views.create_device, name='device_register'),
    path('', views.DeviceList.as_view(), name='device_list'),
    path('device/read/<int:pk>', views.DeviceDetailView.as_view(), name='device_detail'),
    path('device/update/<int:pk>', views.DeviceUpdateView.as_view(), name='update_device'),
    path('device/delete/<id>', views.delete_device, name='device_delete'),
    path('place/add', views.create_place, name='place_register'),
    path('places', views.PlaceList.as_view(), name='place_list'),
    path('place/read/<int:pk>', views.PlaceDetailView.as_view(), name='place_detail'),
    path('place/update/<int:pk>', views.PlaceUpdateView.as_view(), name='update_place'),
    path('place/delete/<int:pk>', views.PlaceDeleteView.as_view(), name='place_delete'),
    path('user/register', views.UserCreateView.as_view(), name='user_register'),
    path('users', views.UserList.as_view(), name='user_list'),
    path('user/<int:pk>', views.DeviceUserDetailView.as_view(), name='user_detail'),
    path('user/edit/<int:pk>', views.DeviceUserUpdateView.as_view(), name='update_user'),
    path('<int:pk>/user', views.UserDeleteView.as_view(), name='user_delete'),
    path('file_upload', views.file_upload, name='file_upload')
]

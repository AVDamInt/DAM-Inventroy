from django.urls import path
from . import views

urlpatterns = [
    path('', views.device_list, name='device_list'),
    path('device/<int:pk>', views.DeviceDetailView.as_view(), name='device_detail'),
    path('device/register', views.DeviceCreateView.as_view(), name='device_register'),
    path('<int:pk>/delete', views.DeviceDeleteView.as_view(), name='device_delete')
    #path('device/<int:pk>', views.device_details, name='device_details'),
]
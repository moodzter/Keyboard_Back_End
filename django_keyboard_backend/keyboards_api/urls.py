from django.urls import path 
from . import views
urlpatterns = [
    path('api/keyboards', views.KeyboardList.as_view(), name='keyboard_list'),
    path('api/keyboards<int:pk>', views.KeyboardDetail.as_view(), name='keyboard_detail'), 
]
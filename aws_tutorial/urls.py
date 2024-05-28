from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='upload'),
    path('success/', views.success, name='success'),
]
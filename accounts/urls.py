from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('customer/<str:pk>/', views.customer),
    path('', views.home),
    path('products/', views.products),
    path('admin/', admin.site.urls),
]

from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('admin/', admin.site.urls),
]

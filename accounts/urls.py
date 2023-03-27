from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('admin/', admin.site.urls),
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]

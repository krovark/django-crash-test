from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('customers/', views.customers),
    path('', views.home),
    path('products/', views.products),
    path('admin/', admin.site.urls),
]

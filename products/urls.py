"""EPMS URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from products import views

app_name = 'product'
urlpatterns = [

    path('products/',views.ProductListView.as_view(),name='products'),
    path('productdetails/<int:pk>',views.ProductDetailView.as_view(),name='productdetails'),
    path('newproduct/',views.ProductCreateView.as_view(), name='newproduct'),
    path('updateproduct/<int:pk>',views.ProductUpdateView.as_view(), name='updateproduct'),
    path('Deleteproduct/<int:pk>',views.ProductDeleteView.as_view(), name='deleteproduct'),

]
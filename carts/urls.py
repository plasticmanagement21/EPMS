from django.contrib import admin
from django.urls import path
from carts import views


app_name = 'cart'
urlpatterns = [
    path('',views.cart,name='cart'),
    path('add_to_cart/<int:pk>',views.add_to_cart,name='add_to_cart'),
    path('remove_from_cart/<int:pk>',views.remove_from_cart,name='remove_from_cart'),
    path('update_cart/<int:pk>',views.update_cart,name='update_cart'),
    
]
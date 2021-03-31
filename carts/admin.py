from django.contrib import admin
from carts import models
# Register your models here.

@admin.register(models.Cart)
class Cart(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'productquantity', 'total_price', 'added_date']


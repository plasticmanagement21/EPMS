from django.contrib import admin
from products import models


# Register your models here.
@admin.register(models.Product)
class Product(admin.ModelAdmin):
    list_display = ['id', 'user', 'productname', 'productimage', 'productprice', 'productdescription', 'productquantity', 'productaddress', 'hugeproduct']

# admin.site.register(models.Product)
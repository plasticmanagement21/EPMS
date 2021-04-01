from django.contrib import admin
from payments import models
# Register your models here.
# admin.site.register(models.Transaction)


@admin.register(models.Transaction)
class Transaction(admin.ModelAdmin):
    list_display = ['made_by','made_on','amount','order_id','checksum']
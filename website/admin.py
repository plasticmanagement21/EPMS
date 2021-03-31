from django.contrib import admin
from website import models

# Register your models here.

@admin.register(models.UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ['id', 'user', 'fname', 'lname', 'mobilenumber', 'address', 'created']

@admin.register(models.ContactUs)
class ContactUs(admin.ModelAdmin):
    list_display = ['id', 'name', 'mobilenumber', 'email', 'subject', 'message']






# admin.site.register(models.User)
# admin.site.register(models.Product)
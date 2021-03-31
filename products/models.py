from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from website.models import UserProfile
# Create your models here.


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    productname = models.CharField(max_length=256)
    productimage = models.ImageField(upload_to='newproduct/image/')
    productprice = models.FloatField()
    productdescription = models.CharField(max_length=256)
    productquantity = models.PositiveIntegerField(default=1)
    productaddress = models.CharField(max_length=256)
    hugeproduct = models.BooleanField(default=False)

    def __str__(self):
        return self.productname

    def get_absolute_url(self):
        return reverse('home')


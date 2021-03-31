from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.utils import timezone
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    productquantity = models.PositiveIntegerField(default=1)
    total_price = models.PositiveIntegerField(default=0)
    added_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username




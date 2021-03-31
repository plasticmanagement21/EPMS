from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    mobilenumber = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    address = models.CharField(max_length=356)
    created = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user) + ' ' + self.fname + self.lname

    def get_absolute_url(self):
        return reverse('userprofilecreate')


###################################################################################################################


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobilenumber = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    subject = models.CharField(max_length=356)
    message = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contactus')


###############################################################################################################        


# class Product(models.Model):
#     productname = models.CharField(max_length=50)
#     productimage = models.ImageField(upload_to='newproduct/image/')
#     productprice = models.IntegerField()
#     productdescription = models.CharField(max_length=500)

#     def __str__(self):
#         return self.productname


################################################################################################################################


# class Product(models.Model):
#     productname = models.CharField(max_length=256)
#     productimage = models.ImageField(upload_to='newproduct/image/')
#     productprice = models.IntegerField()
#     productdescription = models.CharField(max_length=256)

#     def __str__(self):
#         return self.productname

#     def get_absolute_url(self):
#         return reverse('home')
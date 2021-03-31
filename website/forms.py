from django import forms
from website import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ContactUsForm(forms.ModelForm):
    class Meta():
        model = models.ContactUs
        fields = '__all__'


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = models.UserProfile
        fields = '__all__'








# class UserRegistrationForm(forms.ModelForm):
#     class Meta():
#         model = models.User
#         fields = '__all__'

# class ForgotPasswordForm(forms.ModelForm):
#     cnf_password = forms.CharField(max_length=50)
#     class Meta():
#         model = models.User
#         fields = ['email','password']

# class NewProductForm(forms.ModelForm):
#     class Meta():
#         model = models.Product
#         fields = '__all__'



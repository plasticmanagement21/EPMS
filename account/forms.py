from django import forms
from account import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username','password','email']

class ForgotPasswordForm(forms.ModelForm):
    cnf_password = forms.CharField(max_length=50)
    class Meta():
        model = User
        fields = ['email','password']
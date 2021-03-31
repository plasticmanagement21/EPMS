from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from account import forms
import random


# Create your views here.


user=0
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['username'] = username
            return redirect('home')
        else:
            messages.info(request,'Invalid Credentials.') 
            return redirect('account:login')  
    else:
        return render(request,'login.html',{})


##########################################################################################################


def logout(request):
    del request.session['username']
    auth.logout(request)

    return redirect('home')


##########################################################################################################


def register(request):
    if request.method  == 'POST':
        global user
        username = request.POST['username']
        email = request.POST['email']
        request.session['email'] = email
        password1 = request.POST['password']
        password2 = request.POST['password2']
        
        if (len(password1) > 8):
            if password1==password2:
                if User.objects.filter(username=username).exists():
                    #print('username taken')
                    messages.error(request,'Sorry! Username is taken.')
                    return render(request,'register.html',{})
                elif User.objects.filter(email=email).exists():
                    #print('email taken')
                    messages.error(request,'Sorry! Email is taken.')
                    return render(request,'register.html',{})
                else:
                    user = forms.UserRegistrationForm(request.POST)
                    otp = random.randint(111111,999999)
                    request.session['usr_otp'] = otp
                    if user.is_valid():
                        password = user.cleaned_data.get('password')
                        user.save(commit=False).set_password(password)
                        mail = request.POST.get('email')
                        send_mail(
                                'OTP',
                                f'Here is the OTP to complete registration {otp}.',
                                settings.EMAIL_HOST_USER,
                                [mail],
                                fail_silently=False,)
                    else:
                        messages.error(request,'Invalid Input')
                        return render(request,'register.html',{})
                    return render(request,'otpverify.html',{})
            else:
                messages.error(request,'Password not matched.')
                return render(request,'register.html',{})
        else:
            messages.info(request,'Password must have 8 characters or more.')
            return render(request,'register.html',{})
    else:
        form = forms.UserRegistrationForm()
        return render(request,'register.html',{'form':form})


##########################################################################################################


def otpverify(request):
    #otp = request.POST.get('otp')
    otp = request.session['usr_otp']
    #print(otp)
    uotp = int(request.POST['eotp'])
    if otp == uotp:
        user.save()
        del request.session['usr_otp']
        del request.session['email']
        return render(request,'login.html',{})
    else:
        messages.error(request,'Invalid OTP')
        return render(request,'otpverify.html',{})



##########################################################################################################
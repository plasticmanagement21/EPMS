from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import (CreateView, ListView, UpdateView, DeleteView, DetailView)
from django.contrib.auth.models import User, auth
from django.contrib import messages
from products import models
from django.db.models import Q
from website.models import ContactUs, UserProfile
from website import forms
# Create your views here.


class ProductListView(ListView):
    model = models.Product
    template_name = 'home.html'
    context_object_name = 'objects'
    ordering = ['id']
    paginate_by = 4
    paginate_orphans = 1
    queryset = model.objects.all()


##########################################################################################################


def cart(request):
    return render(request,'cart.html',{})


##########################################################################################################


def aboutus(request):
    return render(request,'aboutus.html',{})


##########################################################################################################

def contactus(request):

    if request.method == 'POST':
        form = forms.ContactUsForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.info(request, 'Thanks for connecting with us.')
            return render(request, 'contactus.html',{})
        else:
            message.info(request,'Invalid Entry. Please try again.')
            return render(request, 'contactus.html', {})
    else:
        form = forms.ContactUsForm()
        return render(request, 'contactus.html',{'form':form})

##########################################################################################################


class SearchView(ListView):
    model = models.Product
    template_name = 'search.html'
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get('keyword')
        srt = self.request.GET.get('sorting')
        if srt == 'lowprice':
            results = models.Product.objects.filter(Q(productname__icontains=kw) | Q(productdescription__icontains=kw) | Q(productaddress__icontains=kw)).order_by('productprice')
        elif srt == 'highprice':
            results = models.Product.objects.filter(Q(productname__icontains=kw) | Q(productdescription__icontains=kw) | Q(productaddress__icontains=kw)).order_by('-productprice')
        else:
            results = models.Product.objects.filter(Q(productname__icontains=kw) | Q(productdescription__icontains=kw) | Q(productaddress__icontains=kw)).order_by('id')
        context['results'] = results
        return context

##############################################################################################################


class UserProfileCreateView(CreateView):
    model = UserProfile
    fields = '__all__'
    template_name = 'userprofile_form.html'

    def post(self, request):
        form = forms.UserProfileForm(request.POST)
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.user = request.user
            userprofile.created = True

            userprofile.save()
            messages.info(request, 'Profile created successfully.')
            return render(request, 'profilecreatedsuccessfully.html',{})
        else:
            messages.info(request, 'Invalid Details')
            return render(request, 'userprofile_form.html',{})

    def get(self,request):
        form = forms.UserProfileForm()
        user = request.user
        #print(user)
        if UserProfile.objects.filter(user=user).exists():
            instance = UserProfile.objects.filter(user=user)
            for object in instance:
                obj = object
            #print(obj,'#################################################################')
            return render(request, 'userprofile_form.html',{'instance':obj})
        else:
            return render(request, 'userprofile_form.html',{})
            



class UserProfileUpdateView(UpdateView):
    model = UserProfile
    fields = ['fname', 'lname', 'mobilenumber', 'address']
    template_name = 'userprofile_form.html'
    context_object_name = 'object'


























































































# class ProductListView(ListView):
#     model = models.Product
#     template_name = 'home.html'
#     context_object_name = 'objects'


# #########################################################################################################


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('home')
#         else:
#             messages.info(request,'Invalid Credentials.') 
#             return redirect('login')  
#     else:
#         return render(request,'login.html',{})


##########################################################################################################

# def logout(request):
#     auth.logout(request)
#     return redirect('home')

# ##########################################################################################################


# def register(request):
# #     if request.method=='POST':
# #         form = forms.UserRegistrationForm(request.POST)
# #         if form.is_valid():
# #             form.save(commit=True)
# #             return HttpResponse('Details Register.')
# #         else:
# #             return HttpResponse('Details Invalid\nTry Again.')
# #     else:
#     if request.method  == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         if password1==password2:
#             if User.objects.filter(username=username).exists():
#                 print('username taken')
#                 return render(request,'register.html',{})
#             elif User.objects.filter(email=email).exists():
#                 print('email taken')
#                 return render(request,'register.html',{})
#             else:
#                 user = User.objects.create_user(username=username, password=password1, email=email)
#                 user.save()
#                 print('form saved')
#                 return redirect('login')
#         else:
#             return HttpResponse('Password didn\'t matched.')
#     else:
#         return render(request,'register.html',{})


# #########################################################################################################


# def products(request):
#     return render(request,'products.html',{})


# #########################################################################################################


# def newproduct(request):
#     form = forms.NewProductForm()
#     if request.method == 'POST':
#         form = forms.NewProductForm(request.POST,request.FILES)
#         if form.is_valid():
#             newproduct = form.save()
#             if 'productimage' in request.FILES:
#                 newproduct.productimage = request.FILES['productimage']

#             newproduct.save()
#             return HttpResponse('Product Added')
#             pass
#         else:
#             return HttpResponse(form.errors)
#     else:
#         return render(request,'newproduct.html',{'form':form})


##########################################################################################################


# def forgotpassword(request):
#      return render(request,'forgotpassword.html',{})


##########################################################################################################


# class ProductCreateView(CreateView):
#     model = models.Product
#     fields = '__all__'
#     template_name = 'newproduct.html'


##########################################################################################################


# class ProductDetailView(DetailView):
#     model = models.Product
#     #fields = '__all__'
#     template_name = 'productdetails.html'


##########################################################################################################





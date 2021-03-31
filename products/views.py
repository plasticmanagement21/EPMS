from django.shortcuts import render,redirect
from django.http import HttpResponse
from products import forms
from products import models
from django.views.generic import (CreateView, ListView, UpdateView, DeleteView, DetailView)
from django.contrib.auth.models import User, auth
from django.urls import reverse_lazy
from django.contrib import messages
from website.models import UserProfile

# Create your views here.


class ProductCreateView(CreateView):
    model = models.Product
    fields = '__all__'
    template_name = 'newproduct.html'

    def post(self,request):
        form = forms.NewProductForm()
        if request.method == 'POST':
            form = forms.NewProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.user = request.user
                
                if 'productimage' in request.FILES:
                    product.productimage = request.FILES['productimage']

                product.save()
                return redirect('home')
            else:
                #print(form.errors)
                messages.error(request,'Invalid Details. Please try again.')
                return render(request, 'newproduct.html',{'form': form})
        else:
            return render(request, 'newproduct.html', {'form': form})

    
##########################################################################################################


class ProductListView(ListView):
    model = models.Product
    template_name = 'products.html'
    context_object_name = 'objects'
    paginate_by = 4
    paginate_orphans = 1
    queryset = model.objects.all()


##########################################################################################################


class ProductDetailView(DetailView):
    model = models.Product
    #fields = '__all__'
    template_name = 'productdetails.html'


##########################################################################################################


class ProductUpdateView(UpdateView):
    model = models.Product
    fields = ['productprice','productdescription','productimage','productname', 'productaddress', 'hugeproduct','productquantity']
    template_name = 'newproduct.html'



##########################################################################################################


class ProductDeleteView(DeleteView):
    model = models.Product
    template_name = 'deleteproduct.html'
    success_url = reverse_lazy('product:products')


##########################################################################################################
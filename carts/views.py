from django.shortcuts import render,redirect
from products.models import Product
from django.contrib.auth.models import User
from carts.models import Cart
from django.contrib import messages
# Create your views here.

def add_to_cart(request,pk):
    #print(pk)
    product = Product.objects.get(pk=pk)
    user = User.objects.get(username=request.user.username)
    if Cart.objects.filter(product=product).exists():
        for object in Cart.objects.filter(product=product):
            productquantity = object.productquantity + 1
        Cart.objects.filter(product=product).update(productquantity=productquantity)
    else:
        Cart.objects.create(user=user,product=product,total_price=product.productprice)
    return redirect('cart:cart')

def cart(request):
    net_total_price = 0
    user = User.objects.get(username=request.user.username) 
    carts = Cart.objects.filter(user=user)
    item_in_carts = carts.count()
    for i in carts:
        subtotal = 0
        subtotal = subtotal + i.productquantity * i.product.productprice
        i.total_price =subtotal
        i.save()
        net_total_price = net_total_price + i.total_price
    
        
    request.session['total-cart'] = len(carts)
    return render(request,'cart.html',{'carts':carts,'net_total_price':net_total_price, 'item_in_carts':item_in_carts})

def update_cart(request,pk):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(username=request.user.username)
    cart = Cart.objects.get(user=user,product=product)
    action = request.GET.get('action')
    if action == "decrease":
        if cart.productquantity == 1:
            messages.info(request, 'Oops! You can remove product by using \' REMOVE \' button.' )
        else:
            cart.productquantity = cart.productquantity - 1
            cart.save()
    else:
        if cart.productquantity == cart.product.productquantity:
            messages.info(request, 'Only'+ ' ' + str(cart.product.productquantity) + ' ' + str(cart.product.productname) + ' ' + 'are' + ' ' + 'available.')
        else:
            cart.productquantity = cart.productquantity + 1
            cart.save()
    return redirect('cart:cart')


def remove_from_cart(request,pk):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(username=request.user.username)
    cart = Cart.objects.get(user=user,product=product)
    cart.delete()
    return redirect('cart:cart')
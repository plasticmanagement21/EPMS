"""EPMS URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from website import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.ProductListView.as_view(),name='home'),

    path('account/',include('account.urls')),
    path('userprofilecreate/', views.UserProfileCreateView.as_view(), name='userprofilecreate'),
    path('userprofileupdate/<int:pk>', views.UserProfileUpdateView.as_view(), name='userprofileupdate'),

    path('products/',include('products.urls')),
    path('cart/',include('carts.urls')),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contactus/',views.contactus,name='contactus'),

    path('passwordresetdone/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('passwordresetconfirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('passwordresetcomplete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    path('search/', views.SearchView.as_view(), name='search'),
    path('paytm/', include('payments.urls')),


    



    # path('login/',views.login,name='login'),
    # path('logout/',views.logout,name='logout'),
    # path('register/',views.register,name='register'),
    # path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    # path('newproduct/',views.newproduct,name='newproduct'),
    # path('products/',views.ProductListView.as_view(),name='products'),
    # path('productdetails/<int:pk>',views.ProductDetailView.as_view(),name='productdetails'),
    # path('newproduct/',views.ProductCreateView.as_view(), name='newproduct'),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
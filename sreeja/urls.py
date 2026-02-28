"""
URL configuration for sreeja project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from userapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup, name='signup'),
    path('',login, name='login'),
    path('home/', home, name='home'),
    path('home/orders/', orders, name='orders'),
    path('user/account', account, name='account'),
    path('user/update/profile', update_profile, name='update_profile'),
    path('user/update/password', update_password, name='update_pass'),
    path('user/SEARCH/', search, name='search'),
    path('logout/', logout, name='logout'), 
    path('cart/', cart, name='cart'), 
    path('add/to/cart/<int:ele>', add_cart, name='add_cart'), 
    path('remove/from/cart/<int:ele>', remove_cart, name='remove_cart'), 
    path('place/order/<int:ele>', place_order, name='place_order'), 
    path('cancel/order/<int:ele>', cancel_order, name='cancel_order'), 
    path('filter/<str:_type>', kind, name='kind'),

]
urlpatterns += static(settings.STATIC_URL ,document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL  ,document_root = settings.MEDIA_ROOT)
